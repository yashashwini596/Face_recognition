from src.face_recognition import compare_faces

dataset = "dataset"

test_image = "test.jpg"

person = compare_faces(test_image, dataset)

print("Recognized Person:", person)