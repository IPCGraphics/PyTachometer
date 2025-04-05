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
            self.Tachometer.SetValue(self.current_RPM)
            self.Tachometer.update_display()

    
    def draw(self):
        """
        Updates the display of the tachometer.

        Returns:
            np.ndarray: The updated base image with the tachometer overlayed.
        """
        self.speed_gauge.update_display()


    def set_RPM(self, RPM):
        """
        Updates the RPM value.

        Parameters:
            RPM (int): The new RPM value.
        """
        if( self.current_RPM != RPM):
            self.current_RPM = RPM
            self.Tachometer.SetValue(RPM)
            self.Tachometer.update_display()
    
    
if __name__ == "__main__":
        # Define the size of the main window
        imagename = 'tachometer'
        window_size = (500, 800, 3)
        MaxRPM = 6000
        MinRPM = 0
        RPM = 0
        imagecontainer = np.zeros(window_size, dtype=np.uint8)
        imagecontainer[:,:] = (0, 0, 0)  # Set the background color to black
        # Create an instance of the Tachometer class
        tachometer = Tachometer(image=imagecontainer, type="analog", MaxValue=MaxRPM)
        # Create window image
        cv2.namedWindow(imagename)
        cv2.imshow(imagename, imagecontainer)
        
        while True:
            # Display the updated image in the window
            # #cv2.imshow(imagename, imagecontainer)
            # Wait for a key press
            # 0xFF is used to mask the key value to get the last 8 bits
            key = cv2.waitKey(1) & 0xFF

            #exit if 'q' is pressed
            if key == ord('q'):
                break
            
            if key == ord('a'):
                # Set the RPM value to 0
                RPM = int(0)
        
            if key == ord('b'):
                # Set the RPM value to 25% of MaxRPM
                RPM = int((MaxRPM * 0.25))

            if key == ord('c'):
                # Set the RPM value to 50% of MaxRPM
                RPM = int((MaxRPM * 0.50))
            
            if key == ord('d'):
                # Set the RPM value to 75% of MaxRPM
                RPM = int((MaxRPM * 0.75))
            
            if key == ord('e'):
                # Set the RPM value to 100% of MaxRPM
                RPM = int(MaxRPM)
        
            if key == ord('+'):
                # update RPM value
                RPM = int(RPM + 500)
                if RPM > MaxRPM:
                    RPM = MaxRPM
            
            if key == ord('-'):
                # update RPM value
                RPM = int(RPM - 500)
                if RPM < MinRPM:
                    RPM = MinRPM
            # Update the tachometer RPM value
            tachometer.set_RPM(RPM)
        
            cv2.imshow(imagename, imagecontainer)
        
        cv2.destroyAllWindows()
