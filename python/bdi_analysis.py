import pandas as pd
import matplotlib.pyplot as plt

# 读取完整的 BDI 历史数据
file_path = "../excel/Baltic Dry Index Historical Data.csv"

try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"找不到文件：{file_path}")
    print("请检查文件名和文件位置是否正确。")
    raise SystemExit

# 检查必要列是否存在
required_columns = ["Date", "Price"]
missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    print("数据中缺少必要列：", missing_columns)
    print("当前列名：", df.columns.tolist())
    raise SystemExit

# 日期转换
df["Date"] = pd.to_datetime(
    df["Date"],
    format="%m/%d/%Y",
    errors="coerce"
)

# 清洗价格字段
df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace(",", "", regex=False)
)

df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# 删除空值
df = df.dropna(subset=["Date", "Price"])

# 按日期排序
df = df.sort_values("Date").reset_index(drop=True)

# 显示数据摘要
print("Cleaned data preview:")
print(df[["Date", "Price"]].head())

print("\nData summary:")
print("Rows:", len(df))
print("Start date:", df["Date"].min())
print("End date:", df["Date"].max())

# 画图
plt.figure(figsize=(12, 6))
plt.plot(df["Date"], df["Price"])
plt.title("Baltic Dry Index (BDI) Monthly Trend, 2020-2026")
plt.xlabel("Date")
plt.ylabel("BDI Points")
plt.xticks(rotation=45)
plt.tight_layout()

# 保存图片
output_path = "../images/bdi_trend_python.png"
plt.savefig(output_path, dpi=300)
print(f"\n图表已保存到：{output_path}")

plt.show()