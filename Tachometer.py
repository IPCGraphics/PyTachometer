import cv2
import numpy as np
from Lib.Graphics.AnalogGauge import AnalogGauge

class Tachometer:
    def __init__(self, image: np.ndarray, type="analog", MaxValue=6000):
        """
        Initializes the Tachometer instance.

        Parameters:
            image (np.ndarray): The main window image (background).
            type (str): The type of tachometer ("analog" or other types).
            MaxValue (int): The maximum speed value.
            MinValue (int): The minimum speed value.
        """
        self.type = type
        self.base_image = image
        self.MaxRPM = MaxValue
        self.current_RPM = 0

        if self.type == "analog":
            self.Tachometer = AnalogGauge(
                image=self.base_image,
                max_value=self.MaxRPM,
                min_value=0,
                minor_marks=1000,
                units='RPM',
                arch=180,
                phase=180)
            self.Tachometer.needle_position_range = self.current_RPM

    
    def draw(self):
        """
        Updates the display of the tachometer.

        Returns:
            np.ndarray: The updated base image with the tachometer overlayed.
        """
        # Draw the tachometer gauge
        return self.Tachometer.update_display()
    
    def set_RPM(self, RPM):
        """
        Updates the RPM value.

        Parameters:
            RPM (int): The new RPM value.
        """
        if( self.current_RPM != RPM):
            self.current_RPM = RPM

        self.Tachometer.needle_position_range = RPM
    
    
if __name__ == "__main__":
        # Define the size of the main window
        window_width = 800
        window_height = 600

        # Create a blank image for the main window
        main_window_image = np.zeros((window_height, window_width, 3), dtype=np.uint8)

        # Create an instance of the Tachometer class
        tachometer = Tachometer(main_window_image, type="analog", MaxValue=6000)

        # Set the RPM value
        tachometer.set_RPM(3000)

        # Draw the tachometer on the main window image
        updated_image = tachometer.draw()

        # Display the updated image in a window
        cv2.imshow("Tachometer", updated_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
