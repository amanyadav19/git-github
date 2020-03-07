import cv2
I = imread('img2.jpg');
b = dec2bin(I); 
du = bin2dec(b);
du = reshape(du,size(I)); 
imwrite(uint8(du), 'du.jpg');

I = imread('du.jpg');
imshow(du)