def information(v, λ):
    frequency = (v / λ)
    print(f"Frequency: {frequency:.2f} Hz")
    
    if frequency > 7:
        print("Check blood vessels")
    elif 2 < frequency <= 7:
        print("Check internal organs")
    else:
        print("Check fetus")

    return frequency

information(10, 2.5)
