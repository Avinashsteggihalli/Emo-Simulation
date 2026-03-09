## Project name: EL Robo | Emo Like Robot

to get idea -(https://youtu.be/abqUMxj-1WI?si=yS3m6AbnimlhUvYT)

### Task 1:(simulation in pc)
 - -1 Get Better Laptop
    * for now choosed-(appx Rs. 1L) | HDFC Loan 81k (2k/5yr[60m])+ 20k slice(2k/12m)
        Lenovo LOQ 2024, 
        Intel Core i5-13450HX, 
        13th Gen, 
        NVIDIA RTX 4050-6GB, 
        16GB RAM, 
        512GB SSD, 
        FHD 144Hz, 
        15.6"/39.6cm, 
        Windows 11, 
        Office Home 2024, 
        Grey, 
        2.4Kg, 
        83DV018JIN, 
        1Yr ADP Free Gaming Laptop


 0) Run the main.py file
    * required 'face_recognition' library.✅
    * for that lib > dlib > Visual Studio Build Tools 2022 > Include: MSVC v143, Windows 10/11 SDK, C++ CMake tools for Windows. ✅ 

    * if `dlib` build still fails on Windows, use this working setup inside `robo_env`:
      ```powershell
      .\robo_env\Scripts\python -m pip install --upgrade pip
      .\robo_env\Scripts\python -m pip install dlib-bin
      .\robo_env\Scripts\python -m pip install face_recognition --no-deps
      .\robo_env\Scripts\python -m pip install click numpy pillow face-recognition-models
      .\robo_env\Scripts\python -c "import dlib, face_recognition; print(dlib.__version__, face_recognition.__version__)"
      ```
    * Error- dataset avinash.jpg not found ✅ 
    * 

 1) Set Anaconda AI/ML libraries VE
    * for faster project building
    * becoz it contain pre-installed AI/ML related libraries.
    * reduce time for solving error in library installation.

 2) my_face (Sample Data) to Machine to learn

 3) Training my_face to Machine/Computer

 4) Face Detection 

 5) Face Recognition (Avinash [me]) 
 
 6) It has to show smile face(emoji/animation) and greet.("Hi Avinash!!) 
