traffic_colour = input("Choose traffic colour ")
zebra_crossing_animation = input("Choose animation ")
if (traffic_colour == "Green" or traffic_colour == "green") and (zebra_crossing_animation == "Stopping" or zebra_crossing_animation == "stopping"):
    print("You can't cross the road")
elif (traffic_colour == "Red" or traffic_colour == "red") and (zebra_crossing_animation == "Moving" or zebra_crossing_animation == "moving"):
    print("You can cross the road")
elif (traffic_colour == "Yellow" or traffic_colour == "yellow") and (zebra_crossing_animation == "Moving" or zebra_crossing_animation == "moving"):
    print("Wait! the cars are still moving you can cross the road when the cars stop")
elif (traffic_colour == "Yellow" or traffic_colour == "yellow") and (zebra_crossing_animation == "Stopping" or zebra_crossing_animation == "stopping"):
    print("You can cross when the cars stop.")
elif (traffic_colour == "Red" or traffic_colour == "red") and (zebra_crossing_animation == "Stopping" or zebra_crossing_animation == "stopping"):
    print("I think the traffic light is broken")
elif (traffic_colour == "Green" or traffic_colour == "green") and (zebra_crossing_animation == "Moving" or zebra_crossing_animation == "moving"):
    print("I think the traffic light is broken")
