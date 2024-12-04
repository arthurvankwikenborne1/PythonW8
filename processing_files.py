import sqlite3

def list_of_tracks(file,path_db,path_output_file):
	connection=sqlite3.connect("path_db")
	cursor = connection.cursor()
	query = """
	SELECT 
		t.Name as TrackName,
		al.Title as AlbumName,
		ar.Name as ArtistName
	FROM
		tracks t
	JOIN 
		albums al ON t.AlbumId = al.AlbumId
	JOIN
		artists ar ON al.ArtistId = ar.ArtistId
	WHERE
		t.Name = ?;
	"""

	cursor.execute(query, (track_name,))
	results = cursor.fetchall
	return results
