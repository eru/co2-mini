import co2meter as co2


def main() -> None:
    mon = co2.CO2monitor(bypass_decrypt=True)
    data = mon.read_data()
    # 1: co2, 2: temp
    print(data[1], round(data[2], 1))


if __name__ == "__main__":
    main()
