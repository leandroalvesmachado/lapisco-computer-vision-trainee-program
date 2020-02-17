import cv2

# caminho da imagem e leitura da imagem para uma matriz
img_dir = '../INRIA_Person_Dataset/crop_000010.png'
img = cv2.imread(img_dir)

# abre uma janela com a imagem
# waitKey funcao ligada ao teclado, tempo em milissegundos, passar 0, aguarda indefinidamente por um toque de tecla
# destroyAllWindows destroi todas as janelas criadas
# imwrite para salvar uma imagem
cv2.imshow('image', img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
cv2.imwrite('image_save.png', img)