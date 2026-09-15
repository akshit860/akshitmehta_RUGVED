import math
import matplotlib.pyplot as plt

class ContinuousUnicycleRobot:
    def __init__(self, x=0.0, y=0.0, theta=0.0, dt=0.01):
        self.x = x
        self.y = y
        self.theta = theta
        self.dt = dt
        self.history = [(self.x, self.y, self.theta)]

    def execute_velocity_command(self, v, omega, duration):
        init_state = f"({self.x:.2f}, {self.y:.2f}, {math.degrees(self.theta):.2f}°)"
        steps = int(duration / self.dt)
        for _ in range(steps):
            self.x += v * math.cos(self.theta) * self.dt
            self.y += v * math.sin(self.theta) * self.dt
            self.theta += omega * self.dt
            self.theta = math.atan2(math.sin(self.theta), math.cos(self.theta))
            self.history.append((self.x, self.y, self.theta))
            
        final_state = f"({self.x:.2f}, {self.y:.2f}, {math.degrees(self.theta):.2f}°)"
        cmd_str = f"v={v:.2f}, w={omega:.2f}, t={duration:.2f}s"
        print(f"Start: {init_state} | Command: {cmd_str} | End: {final_state}")

    def plot_trajectory(self):
        xs = [h[0] for h in self.history]
        ys = [h[1] for h in self.history]
        thetas = [h[2] for h in self.history]
        
        plt.figure(figsize=(8, 8))
        plt.plot(xs, ys, label="Continuous Trajectory", color="blue", linewidth=1.5, zorder=1)
        step = max(1, len(self.history) // 30)
        xs_sub = xs[::step]
        ys_sub = ys[::step]
        us = [math.cos(th) for th in thetas[::step]]
        vs = [math.sin(th) for th in thetas[::step]]
        
        plt.quiver(xs_sub, ys_sub, us, vs, color="red", scale=20, width=0.004, label="Heading", zorder=2)
        plt.scatter(xs[0], ys[0], color="green", s=100, label="Start", zorder=3)
        plt.scatter(xs[-1], ys[-1], color="magenta", s=100, label="End", zorder=3)
        
        plt.title("Continuous Unicycle Model Trajectory (Task 4)")
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
    print("--- Continuous Unicycle Motion Model Setup ---")
    start_x = get_float_input("Start X [default 0.0]: ", 0.0)
    start_y = get_float_input("Start Y [default 0.0]: ", 0.0)
    start_deg = get_float_input("Start Heading in Degrees [default 0.0°]: ", 0.0)
    dt_val = get_float_input("Integration Time Step dt [default 0.01s]: ", 0.01)

    robot = ContinuousUnicycleRobot(x=start_x, y=start_y, theta=math.radians(start_deg), dt=dt_val)

    print("\nEnter velocity commands in format:")
    print("Example: '1.5 45 2.0')")
    print("Type 'done' once completed.\n")

    while True:
        cmd = input("Enter (v, omega_deg, duration): ").strip()
        if cmd.lower() == "done":
            break
        if not cmd:
            continue
            
        try:
            parts = cmd.split()
            if len(parts) != 3:
                print("Error: Expecting 3 values (v, omega_deg, duration).")
                continue
            
            v = float(parts[0])
            omega_deg = float(parts[1])
            duration = float(parts[2])

            omega_rad = math.radians(omega_deg)
            robot.execute_velocity_command(v, omega_rad, duration)

        except ValueError:
            print("Invalid input values.")

    if len(robot.history) > 1:
        print("\nPlotting continuous trajectory...")
        robot.plot_trajectory()
    else:
        print("No velocity commands executed. Exiting without plotting.")