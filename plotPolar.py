import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from globali import angle, distance

def plot_lidar_data(angles, distances):
    """
    Plots LiDAR data in polar coordinates (angle vs. distance).
    
    Parameters:
        angles (list or numpy array): List or array of angles in degrees.
        distances (list or numpy array): List or array of distances corresponding to each angle.
    """
    # Convert angles from degrees to radians
    angles_rad = np.deg2rad(angles)
    
    # Create the polar plot
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    
    # Plot the data
    #ax.scatter(angles_rad, distances, c=distances, cmap='viridis', s=20)
    ax.plot(angles_rad, distances, color='b', marker='o', linestyle='-', markersize=5)

    
    # Add labels and grid
    ax.set_theta_zero_location('N')  # Set zero to be at the top (North)
    ax.set_theta_direction(-1)  # Set the angle direction to be clockwise
    ax.set_rlabel_position(0)  # Set radial labels to be at 0 degrees
    
    # Labeling
    ax.set_title("LiDAR Data (Angle vs Distance)")
    ax.set_xlabel("Angle (degrees)")
    ax.set_ylabel("Distance")
    
    # Show plot
    plt.show()

def plot_lidar_live():
    # Set up the plot
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.set_theta_zero_location('N')  # Zero angle at the top
    ax.set_theta_direction(-1)  # Clockwise direction
    
    line, = ax.plot([], [], color='b', marker='o', linestyle='-', markersize=5)
    
    # Set up plot limits (you can adjust these as necessary)
    ax.set_xlim(0, 2 * np.pi)  # Angle (in radians, 0 to 2pi)
    ax.set_ylim(0, 4000)  # Distance (radius)
    
    def init():
        """Initialize an empty plot."""
        line.set_data([], [])
        return line,
    
    def update(frame,angle,distance):
        #global angle, distance
        """Update the plot with new LiDAR data."""
        # Replace this with your actual data stream
        #angles = np.linspace(0, 360, 100)  # Example angles from 0 to 360 degrees
        #distances = np.random.uniform(1, 10, 100)  # Example distances between 1 and 10 units
        
        # Convert angles to radians
        angles_rad = np.deg2rad(angle)
        
        # Update the plot data
        line.set_data(angles_rad[:500], distance[:500])
        angle.clear()
        distance.clear()
        
        return line,

    # Create the animation
    ani = FuncAnimation(fig, update, init_func=init, fargs=(angle, distance), interval=500, blit=True, cache_frame_data=False)

    # Show the plot
    plt.show()

# Example usage:
""" angles = np.linspace(0, 360, 100)  # Example angles from 0 to 360 degrees
distances = np.random.uniform(1, 10, 100)  # Example distances between 1 and 10 units
plot_lidar_data(angles, distances)  """