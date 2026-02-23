1. Arsitektur 
	1. PHP -> CI4
	2. System Requirement 
		1. Server Lokal
		2. Server Eksternal -> Jasa Hosting ( Untuk saat ini pakai Domain aku aja )
			1. http://oort678.my.id/
2. Cara Masuk 
	   1. NIP / NIS atau Email 
		   1. Jika Email maka perlu bikin akun VIA Google
	   2. 
3. Tampilan Dashboard 
		1. Infografis



----

CREATE TABLE Penilaian(
	Nomor INT AUTO_INCREMENT PRIMARY KEY,
	Kompetensi VARCHAR(500),
	Bobot DECIMAL(2,0),
);

INSERT INTO Penilaian(Kompetensi,Bobot) VALUES 
("Makhorijul Huruf", 5), ("",)

CREATE TABLE Observasi(
	Nomor INT AUTO_INCREMENT PRIMARY KEY,
	Id_Siswa INT,
	Id_Hafalan INT,
	Kompetensi INT,
	Nilai INT,
	FOREIGN KEY Id_Siswa REFFERENCES,
	FOREIGN KEY Id_Hafalan REFFERENCES, 
	FOREIGN KEY Kompetensi REFFERENCES Penilaian(Nomor) 
);

CREATE TABLE RekapNilai(
	Id_Siswa INT PRIMARY KEY,
	Makhroj INT,
	
	
);