def imageTruncation(image, threshold):
    for x in range(len(image)):
        for y in range(len(image[x])):
            if image[x][y] > threshold:
                image[x][y] = threshold
    
    return image