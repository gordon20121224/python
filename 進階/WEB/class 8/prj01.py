#######################模組#######################
import discord  # 匯入 discord 模組
import os  # 匯入 os 模組
from dotenv import load_dotenv  # 匯入 dotenv 模組
from myfunction.myfunction import WeatherAPI  # 匯入 myfunction 模組
import openai  # 匯入 openai 模組

#######################初始化#######################
load_dotenv()  # 載入環境變數
# 建立機器人，並設定intents已接收的指令
intents = discord.Intents.default()
intents.message_content = True  # 允許接收消息內容intents
bot = discord.Client(intents=intents)  # 建立一個dicord 客戶端
tree = discord.app_commands.CommandTree(bot)  # 建立一個指令樹，用於管理slash命令

weather_api = WeatherAPI(os.getenv("WEATHER_API_KEY"))  # 建立天氣API
openai.api_key = os.getenv("OPENAI_API_KEY")  # 設定 openai api key


#######################事件#######################
@bot.event  # 事件
async def on_ready():
    print(f"{bot.user} is ready and online!")
    await tree.sync()  # 同步指令至服务器


@bot.event  # 事件
async def on_message(message):
    channel_id = message.channel.id  # 取得頻道id
    if message.author == bot.user:  # 如果是机器人則略過
        return  # 略過
    if message.content == "hello":
        await message.channel.send("Hello!")  # 回傳消息
    elif channel_id in channel_games:  # 如果頻道存在
        user_input = message.content.strip()  # 取得輸入的內容
        if user_input == "結束游戲":  # 如果輸入的內容是結束游戲
            channel_games.pop(channel_id)  # 刪除頻道
            await message.channel.send("游戲結束！")  # 回傳消息
        else:
            game_data = channel_games[channel_id]["game_data"]  # 取得遊戲資料
            if "history" not in channel_games[channel_id]:  # 如果沒有历史記錄
                channel_games[channel_id]["history"] = []  # 建立历史記錄
            history = channel_games[channel_id]["history"]  # 取得历史記錄
            history.append({"role": "user", "content": user_input})  # 加入历史記錄


# 以頻道為鍵，遊戲狀態為value，這是一個全域變數所有指令都可以讀取
# 如果把字典當作全域變數就不需要宣告global就可以直接修改字典里的數值
channel_games = {}


#######################指令#######################
@tree.command(name="hello", description="Say hello to the bot!")  # 建立指令
async def hello(interaction: discord.Interaction):
    """輸入 hello, 回傳 Hello!"""
    await interaction.response.send_message("Hey!")  # 回傳消息


@tree.command(name="weather", description="取得天氣資訊")  # 建立指令
async def weather(
    interaction: discord.Interaction,
    city: str,
    forecast: bool = False,
    ai: bool = False,
):
    await interaction.response.defer()  # 防止指令被重複執行

    unit_symbol = "C" if weather_api.units == "metric" else "F"

    if not forecast:
        info = weather_api.get_current_weather(city)
        if "weather" in info and "main" in info:
            current_temperature = info["main"]["temp"]
            weather_description = info["weather"][0]["description"]
            icon_code = info["weather"][0]["icon"]
            icon_url = weather_api.get_icon_url(icon_code)

            embed = discord.Embed(
                title=f"{city}的當前天氣",
                description=f"{weather_description}",
                color=0x1E90FF,
            )
            embed.set_thumbnail(url=icon_url)
            embed.add_field(
                name="溫度", value=f"{current_temperature}{unit_symbol}", inline=True
            )
            await interaction.followup.send(embed=embed)
        else:
            await interaction.followup.send(f"找不到**{city}**的天氣資訊")
    else:
        info = weather_api.get_forecast(city)
        if "list" in info:
            if not ai:
                forecast_list = info["list"][:10]
                embeds = []
                for forecast in forecast_list:
                    dt_txt = forecast["dt_txt"]
                    temp = forecast["main"]["temp"]
                    description = forecast["weather"][0]["description"]
                    icon_code = forecast["weather"][0]["icon"]
                    icon_url = weather_api.get_icon_url(icon_code)

                    embed = discord.Embed(
                        title=f"{city}的天氣預報-{dt_txt}",
                        description=f"{description}",
                        color=0x1E90FF,
                    )
                    embed.set_thumbnail(url=icon_url)
                    embed.add_field(
                        name="溫度",
                        value=f"{temp}{unit_symbol}",
                        inline=False,
                    )
                    embeds.append(embed)
                await interaction.followup.send(embeds=embeds)
            else:
                try:
                    response = openai.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {
                                "role": "system",
                                "content": "你是一位專業的氣象分析師，為使用者提供詳細的天氣分析和建議。",
                            },
                            {
                                "role": "user",
                                "content": f"以下是{city}的未來天氣預報，請根據這些數據提供詳細的天氣分析和建議。\n{info}",
                            },
                        ],
                        temperature=0.2,
                    )

                    anaylsis = response.choices[0].message.content

                    await interaction.followup.send(
                        f"**{city}**的天氣分析和建議：\n{anaylsis}"
                    )
                except Exception as e:
                    await interaction.followup.send(f"發生錯誤：{e}")
        else:
            await interaction.followup.send(f"找不到**{city}**的天氣資訊")


@tree.command(name="turtle_game", description="開啟海龜湯遊戲")  # 建立指令
async def turtle_game(interaction: discord.Interaction):
    channel_id = interaction.channel.id  # 取得頻道id
    if channel_id in channel_games:  # 如果頻道已經存在
        await interaction.response.send_message(
            "頻道已經存在，請勿重複開啟"
        )  # 回傳消息
    else:  # 如果頻道不存在, 則建立頻道
        channel_games[channel_id] = {
            "game_data": {
                "question": "一個人在沙漠中發現了一具屍體，旁邊有一根燒過的火柴。發生了什麼事？",
                "answer": "他參加的熱氣球比賽為減了重需要有人跳下去他抽到最短的火柴只好跳下。",
                "solved": False,
            },
            "history": [],
            "current_question": 0,
        }
    await interaction.response.send_message(
        f"""
    遊戲開始!
    題目: {channel_games[channel_id]["game_data"]["question"]}
    請大家開始提問，輸入結束游戲可結束游戲。
    我的回應只會是「是」、「不是」或「無可奉告」。
    """
    )


#######################啟動#######################
def main():
    # 讀取環境變數，並啟動機器人
    bot.run(os.getenv("DC_BOT_TOKEN"))


# 主程式
if __name__ == "__main__":
    main()  # 執行主程式
