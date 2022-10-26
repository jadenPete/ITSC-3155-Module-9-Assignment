import re

def movie_row_regex(title, director, rating):
	return fr"<tr>[ \n]*<td>{re.escape(title)}</td>[ \n]*<td>{re.escape(director)}</td>[ \n]*<td>[ \n]*{re.escape(rating)}[ \n]*</td>[ \n]*</tr>"
