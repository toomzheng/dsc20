"""
DSC 20 Project
Name(s): TODO
PID(s):  TODO
Sources: None
"""

import numpy as np
import os
from PIL import Image
import wave
import struct
# import matplotlib.pyplot as plt

NUM_CHANNELS = 3


# --------------------------------------------------------------------------- #

# YOU SHOULD NOT MODIFY THESE TWO METHODS

def img_read_helper(path):
    """
    Creates an RGBImage object from the given image file
    """
    # Open the image in RGB
    img = Image.open(path).convert("RGB")
    # Convert to numpy array and then to a list
    matrix = np.array(img).tolist()
    # Use student's code to create an RGBImage object
    return RGBImage(matrix)


def img_save_helper(path, image):
    """
    Saves the given RGBImage instance to the given path
    """
    # Convert list to numpy array
    img_array = np.array(image.get_pixels())
    # Convert numpy array to PIL Image object
    img = Image.fromarray(img_array.astype(np.uint8))
    # Save the image object to path
    img.save(path)


# --------------------------------------------------------------------------- #

# Part 1: RGB Image #
class RGBImage:
    """
    Represents an image in RGB format
    """

    def __init__(self, pixels):
        """
        Initializes a new RGBImage object

        # Test with non-rectangular list
        >>> pixels = [
        ...              [[255, 255, 255], [255, 255, 255]],
        ...              [[255, 255, 255]]
        ...          ]
        >>> RGBImage(pixels)
        Traceback (most recent call last):
        ...
        TypeError

        # Test instance variables
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img.pixels
        [[[255, 255, 255], [0, 0, 0]]]
        >>> img.num_rows
        1
        >>> img.num_cols
        2
        """
        # Raise exceptions here
        # Check if pixels is a list with at least one element
        if not isinstance(pixels, list) or len(pixels) == 0:
            raise TypeError()
        
        # Check if all rows are lists with at least one element
        if not all(isinstance(row, list) and len(row) > 0 for row in pixels):
            raise TypeError()
        
        # Check if all rows have the same length
        row_lengths = [len(row) for row in pixels]
        if len(set(row_lengths)) != 1:
            raise TypeError()
        
        # Check if all pixels are lists of length 3
        for row in pixels:
            for pixel in row:
                if not isinstance(pixel, list) or len(pixel) != 3:
                    raise TypeError()
                
                # Check if all intensity values are integers between 0-255
                for value in pixel:
                    if not isinstance(value, int) or value < 0 or value > 255:
                        raise ValueError()
        self.pixels = pixels
        self.num_rows = len(pixels)
        self.num_cols = len(pixels[0])

    def size(self):
        """
        Returns the size of the image in (rows, cols) format

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img.size()
        (1, 2)
        """
        return (self.num_rows, self.num_cols)

    def get_pixels(self):
        """
        Returns a copy of the image pixel array

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img_pixels = img.get_pixels()

        # Check if this is a deep copy
        >>> img_pixels                               # Check the values
        [[[255, 255, 255], [0, 0, 0]]]
        >>> id(pixels) != id(img_pixels)             # Check outer list
        True
        >>> id(pixels[0]) != id(img_pixels[0])       # Check row
        True
        >>> id(pixels[0][0]) != id(img_pixels[0][0]) # Check pixel
        True
        """
        return [[[pixel[c] for c in range(3)] for pixel in row] for row in self.pixels]
    
    def copy(self):
        """
        Returns a copy of this RGBImage object

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img_copy = img.copy()

        # Check that this is a new instance
        >>> id(img_copy) != id(img)
        True
        """
        # YOUR CODE GOES HERE #
        return RGBImage.get_pixels

    def get_pixel(self, row, col):
        """
        Returns the (R, G, B) value at the given position

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)

        # Test with an invalid index
        >>> img.get_pixel(1, 0)
        Traceback (most recent call last):
        ...
        ValueError

        # Run and check the returned value
        >>> img.get_pixel(0, 0)
        (255, 255, 255)
        """
        # YOUR CODE GOES HERE #
        if not isinstance(row, int) or not isinstance(col, int):
            raise TypeError()
        if (row < 0 or row not in range(self.num_rows)) or (col < 0 or col not in range(self.num_cols)):
            raise ValueError()
        
        return tuple(self.pixels[row][col])

    def set_pixel(self, row, col, new_color):
        """
        Sets the (R, G, B) value at the given position

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)

        # Test with an invalid new_color tuple
        >>> img.set_pixel(0, 0, (256, 0, 0))
        Traceback (most recent call last):
        ...
        ValueError

        # Check that the R/G/B value with negative is unchanged
        >>> img.set_pixel(0, 0, (-1, 0, 0))
        >>> img.pixels
        [[[255, 0, 0], [0, 0, 0]]]
        """
        if not isinstance(row, int) or not isinstance(col, int):
            raise TypeError()
        if (row < 0 or row not in range(self.num_rows)) or (col < 0 or col not in range(self.num_cols)):
            raise ValueError()
        if not isinstance(new_color, tuple) and isinstance(len(new_color) == 3) and all([isinstance(new_color_pixel, int) for new_color_pixel in new_color]):
            raise TypeError()
        if any(x > 255 for x in new_color):
            raise ValueError()
        
        for i in range(3):
            if new_color[i] >= 0:
                self.pixels[row][col][i] = new_color[i]

# Part 2: Image Processing Template Methods #
class ImageProcessingTemplate:
    """
    Contains assorted image processing methods
    Intended to be used as a parent class
    """

    def __init__(self):
        """
        Creates a new ImageProcessingTemplate object

        # Check that the cost was assigned
        >>> img_proc = ImageProcessingTemplate()
        >>> img_proc.cost
        0
        """
        # YOUR CODE GOES HERE #
        self.cost = 0

    def get_cost(self):
        """
        Returns the current total incurred cost

        # Check that the cost value is returned
        >>> img_proc = ImageProcessingTemplate()
        >>> img_proc.cost = 50 # Manually modify cost
        >>> img_proc.get_cost()
        50
        """
        return self.cost

    def negate(self, image):
        """
        Returns a negated copy of the given image

        # Check if this is returning a new RGBImage instance
        >>> img_proc = ImageProcessingTemplate()
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img_negate = img_proc.negate(img)
        >>> id(img) != id(img_negate) # Check for new RGBImage instance
        True

        # The following is a description of how this test works
        # 1 Create a processor
        # 2/3 Read in the input and expected output
        # 4 Modify the input
        # 5 Compare the modified and expected
        # 6 Write the output to file
        # You can view the output in the img/out/ directory
        >>> img_proc = ImageProcessingTemplate()                            # 1
        >>> img = img_read_helper('img/test_image_32x32.png')                 # 2
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_negate.png')  # 3
        >>> img_negate = img_proc.negate(img)                               # 4
        >>> img_negate.pixels == img_exp.pixels # Check negate output       # 5
        True
        >>> img_save_helper('img/out/test_image_32x32_negate.png', img_negate)# 6
        """
        negated_pixels =  [[[255 - val for val in pixel] for pixel in row] for row in image.get_pixels()]

        return RGBImage(negated_pixels)

    def grayscale(self, image):
        """
        Returns a grayscale copy of the given image

        # See negate for info on this test
        # You can view the output in the img/out/ directory
        >>> img_proc = ImageProcessingTemplate()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_gray.png')
        >>> img_gray = img_proc.grayscale(img)
        >>> img_gray.pixels == img_exp.pixels # Check grayscale output
        True
        >>> img_save_helper('img/out/test_image_32x32_gray.png', img_gray)
        """
        grayscale_pixels = [[[sum((R, G, B))//3] * 3 for R, G, B in row] for row in image.get_pixels()]

        return RGBImage(grayscale_pixels)

    def rotate_180(self, image):
        """
        Returns a rotated version of the given image

        # See negate for info on this test
        # You can view the output in the img/out/ directory
        >>> img_proc = ImageProcessingTemplate()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_rotate.png')
        >>> img_rotate = img_proc.rotate_180(img)
        >>> img_rotate.pixels == img_exp.pixels # Check rotate_180 output
        True
        >>> img_save_helper('img/out/test_image_32x32_rotate.png', img_rotate)
        """
        rotated_pixels = [row[::-1] for row in image.get_pixels()[::-1]]
        return RGBImage(rotated_pixels)

    def get_average_brightness(self, image):
        """
        Returns the average brightness for the given image

        >>> img_proc = ImageProcessingTemplate()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_proc.get_average_brightness(img)
        86
        """
        total_pixels = image.num_rows * image.num_cols
        average_brightness = sum(sum(pixel)//3 for row in image.get_pixels() for pixel in row)//total_pixels
        return average_brightness

    def adjust_brightness(self, image, intensity):
        """
        Returns a new image with adjusted brightness level

        >>> img_proc = ImageProcessingTemplate()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_adjusted.png')
        >>> img_adjust = img_proc.adjust_brightness(img, 1.2)
        >>> img_adjust.pixels == img_exp.pixels # Check adjust_brightness
        True
        >>> img_save_helper('img/out/test_image_32x32_adjusted.png', img_adjust)
        """
        if not isinstance(intensity, float) or intensity < 0:
            raise TypeError()
        # Ensure that the pixel doesn't go out of range and that the intensity multiplied with pixel value turns into an integer
        adjusted_pixels = [[[min(255, int(x * intensity)) for x in val] for val in row] for row in image.get_pixels()]
        return RGBImage(adjusted_pixels)


# # Part 3: Standard Image Processing Methods #
# class StandardImageProcessing(ImageProcessingTemplate):
#     """
#     Represents a standard tier of an image processor
#     """

#     def __init__(self):
#         """
#         Creates a new StandardImageProcessing object

#         # Check that the cost was assigned
#         >>> img_proc = StandardImageProcessing()
#         >>> img_proc.cost
#         0
#         """
#         # YOUR CODE GOES HERE #
#         self.cost = ...

#     def negate(self, image):
#         """
#         Returns a negated copy of the given image

#         # Check the expected cost
#         >>> img_proc = StandardImageProcessing()
#         >>> img_in = img_read_helper('img/square_32x32.png')
#         >>> negated = img_proc.negate(img_in)
#         >>> img_proc.get_cost()
#         5

#         # Check that negate works the same as in the parent class
#         >>> img_proc = StandardImageProcessing()
#         >>> img = img_read_helper('img/test_image_32x32.png')
#         >>> img_exp = img_read_helper('img/exp/test_image_32x32_negate.png')
#         >>> img_negate = img_proc.negate(img)
#         >>> img_negate.pixels == img_exp.pixels # Check negate output
#         True
#         """
#         # YOUR CODE GOES HERE #

#     def grayscale(self, image):
#         """
#         Returns a grayscale copy of the given image

#         """
#         # YOUR CODE GOES HERE #

#     def rotate_180(self, image):
#         """
#         Returns a rotated version of the given image
#         """
#         # YOUR CODE GOES HERE #

#     def adjust_brightness(self, image, intensity):
#         """
#         Returns a new image with adjusted brightness level
#         """
#         # YOUR CODE GOES HERE #

#     def redeem_coupon(self, amount):
#         """
#         Makes the given number of methods calls free

#         # Check that the cost does not change for a call to negate
#         # when a coupon is redeemed
#         >>> img_proc = StandardImageProcessing()
#         >>> img = img_read_helper('img/test_image_32x32.png')
#         >>> img_proc.redeem_coupon(1)
#         >>> img = img_proc.rotate_180(img)
#         >>> img_proc.get_cost()
#         0
#         """
#         # YOUR CODE GOES HERE #


# # Part 4: Premium Image Processing Methods #
# class PremiumImageProcessing(ImageProcessingTemplate):
#     """
#     Represents a paid tier of an image processor
#     """

#     def __init__(self):
#         """
#         Creates a new PremiumImageProcessing object

#         # Check the expected cost
#         >>> img_proc = PremiumImageProcessing()
#         >>> img_proc.get_cost()
#         50
#         """
#         # YOUR CODE GOES HERE #
#         self.cost = ...

#     def pixelate(self, image, block_dim):
#         """
#         Returns a pixelated version of the image, where block_dim is the size of 
#         the square blocks.

#         >>> img_proc = PremiumImageProcessing()
#         >>> img = img_read_helper('img/test_image_32x32.png')
#         >>> img_pixelate = img_proc.pixelate(img, 4)
#         >>> img_exp = img_read_helper('img/exp/test_image_32x32_pixelate.png')
#         >>> img_exp.pixels == img_pixelate.pixels # Check pixelate output
#         True
#         >>> img_save_helper('img/out/test_image_32x32_pixelate.png', img_pixelate)
#         """
#         # YOUR CODE GOES HERE #

#     def edge_highlight(self, image):
#         """
#         Returns a new image with the edges highlighted

#         >>> img_proc = PremiumImageProcessing()
#         >>> img = img_read_helper('img/test_image_32x32.png')
#         >>> img_edge = img_proc.edge_highlight(img)
#         >>> img_exp = img_read_helper('img/exp/test_image_32x32_edge.png')
#         >>> img_exp.pixels == img_edge.pixels # Check edge_highlight output
#         True
#         >>> img_save_helper('img/out/test_image_32x32_edge.png', img_edge)
#         """
#         # YOUR CODE GOES HERE #


# # --------------------------------------------------------------------------- #

# # YOU SHOULD NOT MODIFY THESE THREE METHODS

# def audio_read_helper(path, visualize=False):
#     """
#     Creates an AudioWave object from the given WAV file
#     """
#     with wave.open(path, "rb") as wav_file:
#         num_frames = wav_file.getnframes()  # Total number of frames
#         num_channels = wav_file.getnchannels()  # Number of channels (1 for mono, 2 for stereo)
#         sample_width = wav_file.getsampwidth()  # Number of bytes per sample (e.g., 2 for 16-bit)
        
#         # Read the frames as bytes
#         raw_bytes = wav_file.readframes(num_frames)
        
#         # Determine the format string for struct.unpack()
#         fmt = f"{num_frames * num_channels}{'h' if sample_width == 2 else 'B'}"
        
#         # Convert bytes to a list of integers
#         audio_data = list(struct.unpack(fmt, raw_bytes))

#     return AudioWave(audio_data)


# def audio_save_helper(path, audio, sample_rate = 44100):
#     """
#     Saves the given AudioWave instance to the given path as a WAV file
#     """
#     sample_rate = 44100  # 44.1 kHz standard sample rate
#     num_channels = 1  # Mono
#     sample_width = 2  # 16-bit PCM

#     # Convert list to bytes
#     byte_data = struct.pack(f"{len(audio.wave)}h", *audio.wave)
#     with wave.open(path, "wb") as wav_file:
#         wav_file.setnchannels(num_channels)
#         wav_file.setsampwidth(sample_width)
#         wav_file.setframerate(sample_rate)
#         wav_file.writeframes(byte_data)


# # def audio_visualizer(path, start=0, end=5):
# #     """
# #     Visualizes the given WAV file
# #     x-axis: time (sec)
# #     y-axis: wave amplitude
# #     ---
# #     Parameters: 
# #         path (str): path to the WAV file
# #         start (int): start timestamp in seconds, default 0
# #         end (int): end timestamp in seconds, default 5
# #     """
# #     with wave.open(path, "rb") as wav_file:
# #         sample_freq = wav_file.getframerate()  # Sample rate
# #         n_samples = wav_file.getnframes()  # Total number of samples
# #         duration = n_samples/sample_freq # Duration of audio, in seconds

# #         if any([type(param) != int for param in [start, end]]):
# #             raise TypeError("start and end should be integers.")
# #         if (start < 0) or (start > duration) or (end < 0) or (end > duration) or start >= end:
# #             raise ValueError(f"Invalid timestamp: start and end should be between 0 and {int(duration)}, and start < end.")
        
# #         num_frames = wav_file.getnframes()  # Total number of frames
# #         num_channels = wav_file.getnchannels()  # Number of channels (1 for mono, 2 for stereo)
# #         sample_width = wav_file.getsampwidth()  # Number of bytes per sample (e.g., 2 for 16-bit)
        
# #         # Extract audio wave as list
# #         raw_bytes = wav_file.readframes(num_frames)
# #         fmt = f"{num_frames * num_channels}{'h' if sample_width == 2 else 'B'}"
# #         audio_data = list(struct.unpack(fmt, raw_bytes))

# #         # Plot the audio wave
# #         time = np.linspace(start, end, num=(end - start)*sample_freq)
# #         audio_data = audio_data[start*sample_freq:end*sample_freq]
# #         plt.figure(figsize=(15, 5))
# #         plt.ylim([-32768, 32767])
# #         plt.plot(time, audio_data)
# #         plt.title(f'Audio Plot of {path} from {start}s to {end}s')
# #         plt.ylabel('sound wave')
# #         plt.xlabel('time (s)')
# #         plt.xlim(start, end)
# #         plt.show()


# # --------------------------------------------------------------------------- #

# # Part 5: Multimedia Processing
# class AudioWave():
#     """
#         Represents audio through a 1-dimensional array of amplitudes
#     """
#     def __init__(self, amplitudes):
#         self.wave = amplitudes

# class PremiumPlusMultimediaProcessing(PremiumImageProcessing):
#     """
#         Represents the paid tier of multimedia processing
#     """
#     def __init__(self):
#         """
#         Creates a new PremiumPlusMultimediaProcessing object

#         # Check the expected cost
#         >>> multi_proc = PremiumPlusMultimediaProcessing()
#         >>> multi_proc.get_cost()
#         75
#         """
#         # YOUR CODE GOES HERE #
#         self.cost = ...
    
#     def reverse_song(self, audio):
#         """
#         Reverses the audio of the song.

#         >>> multi_proc = PremiumPlusMultimediaProcessing()
#         >>> audio = audio_read_helper('audio/one_summers_day.wav')
#         >>> audio_reversed = multi_proc.reverse_song(audio)
#         >>> audio_exp = audio_read_helper('audio/exp/one_summers_day_reversed.wav')
#         >>> audio_exp.wave == audio_reversed.wave # Check reverse_song output
#         True
#         >>> audio_save_helper('audio/out/one_summers_day_reversed.wav', audio_reversed)
#         """
#         # YOUR CODE GOES HERE #
    
#     def slow_down(self, audio, factor):
#         """
#         Slows down the song by a certain factor.

#         >>> multi_proc = PremiumPlusMultimediaProcessing()
#         >>> audio = audio_read_helper('audio/one_summers_day.wav')
#         >>> audio_slow = multi_proc.slow_down(audio, 2)
#         >>> audio_exp = audio_read_helper('audio/exp/one_summers_day_slow.wav')
#         >>> audio_exp.wave == audio_slow.wave # Check slow_down output
#         True
#         >>> audio_save_helper('audio/out/one_summers_day_slow.wav', audio_slow)
#         """
#         # YOUR CODE GOES HERE #
    
#     def speed_up(self, audio, factor):
#         """
#         Speeds up the song by a certain factor.

#         >>> multi_proc = PremiumPlusMultimediaProcessing()
#         >>> audio = audio_read_helper('audio/one_summers_day.wav')
#         >>> audio_sped_up = multi_proc.speed_up(audio, 2)
#         >>> audio_exp = audio_read_helper('audio/exp/one_summers_day_sped_up.wav')
#         >>> audio_exp.wave == audio_sped_up.wave # Check speed_up output
#         True
#         >>> audio_save_helper('audio/out/one_summers_day_sped_up.wav', audio_sped_up)
#         """
#         # YOUR CODE GOES HERE #

#     def reverb(self, audio):
#         """
#         Adds a reverb/echo effect to the song.

#         >>> multi_proc = PremiumPlusMultimediaProcessing()
#         >>> audio = audio_read_helper('audio/one_summers_day.wav')
#         >>> audio_reverb = multi_proc.reverb(audio)
#         >>> audio_exp = audio_read_helper('audio/exp/one_summers_day_reverb.wav')
#         >>> audio_exp.wave == audio_reverb.wave # Check reverb output
#         True
#         >>> audio_save_helper('audio/out/one_summers_day_reverb.wav', audio_reverb)
#         """
#         # YOUR CODE GOES HERE #
        
#     def clip_song(self, audio, start, end):
#         """
#         Clips a song based on a specified start and end.
        
#         >>> multi_proc = PremiumPlusMultimediaProcessing()
#         >>> audio = audio_read_helper('audio/one_summers_day.wav')
#         >>> audio_clipped = multi_proc.clip_song(audio, 30, 70)
#         >>> audio_exp = audio_read_helper('audio/exp/one_summers_day_clipped.wav')
#         >>> audio_exp.wave == audio_clipped.wave # Check clip_song output
#         True
#         >>> audio_save_helper('audio/out/one_summers_day_clipped.wav', audio_clipped)
#         """
#         # YOUR CODE GOES HERE #


# # Part 6: Image KNN Classifier #
# class ImageKNNClassifier:
#     """
#     Represents a simple KNNClassifier
#     """

#     def __init__(self, k_neighbors):
#         """
#         Creates a new KNN classifier object
#         """
#         # YOUR CODE GOES HERE #

#     def fit(self, data):
#         """
#         Stores the given set of data and labels for later
#         """
#         # YOUR CODE GOES HERE #

#     def distance(self, image1, image2):
#         """
#         Returns the distance between the given images

#         >>> img1 = img_read_helper('img/steve.png')
#         >>> img2 = img_read_helper('img/knn_test_img.png')
#         >>> knn = ImageKNNClassifier(3)
#         >>> knn.distance(img1, img2)
#         15946.312896716909
#         """
#         # YOUR CODE GOES HERE #

#     def vote(self, candidates):
#         """
#         Returns the most frequent label in the given list

#         >>> knn = ImageKNNClassifier(3)
#         >>> knn.vote(['label1', 'label2', 'label2', 'label2', 'label1'])
#         'label2'
#         """
#         # YOUR CODE GOES HERE #

#     def predict(self, image):
#         """
#         Predicts the label of the given image using the labels of
#         the K closest neighbors to this image

#         The test for this method is located in the knn_tests method below
#         """
#         # YOUR CODE GOES HERE #


# def knn_tests(test_img_path):
#     """
#     Function to run knn tests

#     >>> knn_tests('img/knn_test_img.png')
#     'nighttime'
#     """
#     # Read all of the sub-folder names in the knn_data folder
#     # These will be treated as labels
#     path = 'knn_data'
#     data = []
#     for label in os.listdir(path):
#         label_path = os.path.join(path, label)
#         # Ignore non-folder items
#         if not os.path.isdir(label_path):
#             continue
#         # Read in each image in the sub-folder
#         for img_file in os.listdir(label_path):
#             train_img_path = os.path.join(label_path, img_file)
#             img = img_read_helper(train_img_path)
#             # Add the image object and the label to the dataset
#             data.append((img, label))

#     # Create a KNN-classifier using the dataset
#     knn = ImageKNNClassifier(5)

#     # Train the classifier by providing the dataset
#     knn.fit(data)

#     # Create an RGBImage object of the tested image
#     test_img = img_read_helper(test_img_path)

#     # Return the KNN's prediction
#     predicted_label = knn.predict(test_img)
#     return predicted_label
