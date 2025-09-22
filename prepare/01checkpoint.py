# Name: Izzie Vazquez
# Assignment Name: 01 Checkpoint: Review Python 
# Assignment Description: 
# When you physically exercise to strengthen your heart, you should maintain your heart rate within a range for at least 20 minutes. To find that range, subtract your age from 220. This difference is your maximum heart rate per minute. Your heart simply will not beat faster than this maximum (220 - age). When exercising to strengthen your heart, you should keep your heart rate between 65% and 85% of your heart’s maximum rate.

def heart_rate(age):
    print(f"When you exercise to strengthen your heart, you should keep your heart rate between {((220 - age) * .65):.0f} and {((220 - age) * .85):.0f} beats per minute.")
    return

def main():
    age = int(input("Please enter your age: "))
    heart_rate(age)

if __name__ == "__main__":
    main()
