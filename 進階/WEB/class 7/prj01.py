#######################模組#######################
import discord  # 匯入 discord 模組
import os  # 匯入 os 模組
from dotenv import load_dotenv  # 匯入 dotenv 模組
from myfunction.myfunction import WeatherAPI  # 匯入 myfunction 模組

#######################初始化#######################
load_dotenv()  # 載入環境變數
# 建立機器人，並設定intents已接收的指令
intents = discord.Intents.default()
intents.message_content = True  # 允許接收消息內容intents
bot = discord.Client(intents=intents)  # 建立一個dicord 客戶端
tree = discord.app_commands.CommandTree(bot)  # 建立一個指令樹，用於管理slash命令

weather_api = WeatherAPI(os.getenv("WEATHER_API_KEY"))  # 建立天氣API


#######################事件#######################
@bot.event  # 事件
async def on_ready():
    print(f"{bot.user} is ready and online!")
    await tree.sync()  # 同步指令至服务器


@bot.event  # 事件
async def on_message(message):
    if message.author == bot.user:  # 如果是机器人則略過
        return  # 略過
    if message.content == "hello":
        await message.channel.send("Hello!")  # 回傳消息


#######################指令#######################
@tree.command(name="hello", description="Say hello to the bot!")  # 建立指令
async def hello(interaction: discord.Interaction):
    """輸入 hello, 回傳 Hello!"""
    await interaction.response.send_message("Hey!")  # 回傳消息


@tree.command(name="weather", description="取得天氣資訊")  # 建立指令
async def weather(interaction: discord.Interaction, city: str, forecast: bool = False):
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
            await interaction.followup.send(f"找不到**{city}**的天氣資訊")


#######################啟動#######################
def main():
    # 讀取環境變數，並啟動機器人
    bot.run(os.getenv("DC_BOT_TOKEN"))


# 主程式
if __name__ == "__main__":
    main()  # 執行主程式
