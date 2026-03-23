"""Create a calorie estimator for popular Bengali sweets.
- Rasgulla: 150 calories
- Sandesh: 120 calories
- Mishti Doi: 180 calories
- Chomchom: 200 calories
- If unknown sweet, show ""Calorie information not available"""

sweet = input(" enter the name of sweet you ate : ")
if sweet == "rasgulla":
    print(" 150 cal ")
elif sweet == "sandesh":
    print(" 120 ")
elif sweet == "mishtidoi":
    print(" 180 cal ")
elif sweet == "chomchom":
    print(" 200 ")
else:
    print(" calorie information not available ")               