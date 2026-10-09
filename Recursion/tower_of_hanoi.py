def tower_hanoi(disks, start, end, auxiliary):
    if disks == 1:
        print(f"Move disk {disks} from {start} to {end}")
    else: 
        tower_hanoi(disks-1, start, auxiliary, end)
        print(f"Move disk {disks} from {start} to {end}")
        tower_hanoi(disks-1, auxiliary, end, start)
tower_hanoi(3, "A", "C", "B")