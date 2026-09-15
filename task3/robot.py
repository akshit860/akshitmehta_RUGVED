import math
import matplotlib.pyplot as plt

class DiscreteRobot:
    def __init__(self, x=0.0, y=0.0, theta=0.0):
        self.x = x
        self.y = y
        self.theta = theta
        self.history = [(self.x, self.y, self.theta)]

    def execute_command(self, cmd):
        try:
            parts = cmd.strip().split()
            if len(parts) != 2:
                print("Invalid format")
                return False

            action, val_str = parts[0].lower(), parts[1]
            val = float(val_str)
            
            init_state = f"({self.x:.2f}, {self.y:.2f}, {math.degrees(self.theta):.2f}°)"
            
            if action == "forward":
                self.x += val * math.cos(self.theta)
                self.y += val * math.sin(self.theta)
            elif action == "backward":
                self.x -= val * math.cos(self.theta)
                self.y -= val * math.sin(self.theta)
            elif action == "left":
                self.theta += math.radians(val)
            elif action == "right":
                self.theta -= math.radians(val)
            else:
                print(f"Unknown action '{action}'")
                return False
            
            self.theta = math.atan2(math.sin(self.theta), math.cos(self.theta))
            self.history.append((self.x, self.y, self.theta))
            
            final_state = f"({self.x:.2f}, {self.y:.2f}, {math.degrees(self.theta):.2f}°)"
            print(f"Start: {init_state} | Action: {cmd} | End: {final_state}\n")
            return True

        except ValueError:
            print("Invalid number value")
            return False

    def plot_trajectory(self):
        xs = [h[0] for h in self.history]
        ys = [h[1] for h in self.history]
        thetas = [h[2] for h in self.history]
        
        plt.figure(figsize=(8, 8))
        plt.plot(xs, ys, label="Path", zorder=1)
        plt.scatter(xs, ys, color='blue', s=20)
        us = [math.cos(th) for th in thetas]
        vs = [math.sin(th) for th in thetas]
        plt.quiver(xs, ys, us, vs, color='red', scale=15, width=0.005, label="Heading", zorder=2)
        
        plt.scatter(xs[0], ys[0], color='green', s=100, label="Start", zorder=3)
        plt.scatter(xs[-1], ys[-1], color='magenta', s=100, label="End", zorder=3)
        
        plt.title("Trajectory")
        plt.xlabel("X Position")
        plt.ylabel("Y Position")
        plt.axis("equal")
        plt.grid(True)
        plt.legend()
        plt.show()

def get_float_input(prompt, default=0.0):
    user_val = input(prompt).strip()
    if not user_val:
        return default
    try:
        return float(user_val)
    except ValueError:
        print(f"Invalid entry. Using default value of {default}.")
        return default

if __name__ == "__main__":
    print("Set initial robot pose (press Enter for default 0.0):")
    
    start_x = get_float_input("Start X [default 0.0]: ", 0.0)
    start_y = get_float_input("Start Y [default 0.0]: ", 0.0)
    start_deg = get_float_input("Start Heading in Degrees [default 0.0°]: ", 0.0)
    
    robot = DiscreteRobot(x=start_x, y=start_y, theta=math.radians(start_deg))
    
    print("\n Enter Commands")
    print("Type 'done' to stop entering commands.\n")

    while True:
        cmd = input("Enter command: ").strip()
        if cmd.lower() == "done":
            break
        if not cmd:
            continue
        robot.execute_command(cmd)

    if len(robot.history) > 1:
        print("\nPlotting robot trajectory...")
        robot.plot_trajectory()
    else:
        print("No commands executed. Exiting without plotting.")