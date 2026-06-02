class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        return self.dfs(image, sr, sc, color, image[sr][sc])

    # declare a helper function that will allow us to pass the original_color as a parameter
    def dfs(self, image, sr, sc, color, original_color):
        # get the dimensions of the image
        rows = len(image)
        cols = len(image[0])

        # make sure the indices aren't outside of the image bounds
        if (sr >= rows or sr < 0) or (sc >= cols or sc < 0):
            return image

        # if the current color isn't the same as the color of the starting pixel, stop the flood
        if original_color != image[sr][sc]:
            return image

        # if the color has already been changed, don't proceed
        if image[sr][sc] == color:
            return image
        else:
            # update the color
            image[sr][sc] = color

            # check the pixel's neighbors
            self.dfs(image, sr - 1, sc, color, original_color)
            self.dfs(image, sr + 1, sc, color, original_color)
            self.dfs(image, sr, sc + 1, color, original_color)
            self.dfs(image, sr, sc - 1, color, original_color)

        return image