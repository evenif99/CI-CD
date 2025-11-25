import os

# save_path = input('생성할 폴더 이름 입력 : ')
#
# if not os.path.isdir(save_path): # 폴더가 존재하지 않는 경우
#     os.mkdir(save_path)
# else:
#     print(f'{save_path} 폴더는 존재합니다.')
# # end if

# 특정 디렉토리에 하위 디렉토리 여러 개 생성하기
targetFolder = 'd:\\' # \는 특수 문자라서 \\라고 표시해야 합니다.
parentPath = os.path.join(targetFolder, 'sample')
print(parentPath)

try:
    os.mkdir(parentPath)

    # 반복문을 사용하여 하위 폴더 10개를 만들어 봅니다.
    for idx in range(1, 11):
        newFolder = os.path.join(parentPath, 'folder' + str(idx).zfill(2))
        # print(newFolder)
        os.mkdir(newFolder)

except FileExistsError:
    print('해당 디렉토리가 이미 존재합니다.')
# end try

targetFolder = 'd:\\'
parentPath = os.path.join(targetFolder, 'excercise')
print(parentPath)

try:
    os.mkdir(parentPath)

    folderList = ['alpha', 'bravo', 'delta', 'nova', 'terra', 'pixel', 'orbit', 'matrix', 'spark', 'fusion']

    for fold in folderList:
        newFolder = os.path.join(parentPath, fold)
        os.mkdir(newFolder)

except FileExistsError:
    print('해당 디렉토리가 이미 존재합니다.')
