# nlp-api
Natural language processing api for the processing the text and convert into meaning full information.

request struture:
<host>/nlp/EntityRecognizer/type/sentence

type: all/nouns/verbs/entities

entities:

<table>
	<tr>
		<td>TYPE</td>
		<td>DESCRIPTION</td>
	</tr>
	<tr>
		<td>PERSON</td>
		<td>People, including fictional.</td>
	</tr>
	<tr>
		<td>NORP</td>
		<td>Nationalities or religious or political groups.</td>
	</tr>
	<tr>
		<td>FAC</td>
		<td>Buildings, airports, highways, bridges, etc.</td>
	</tr>
	<tr>
		<td>ORG</td>
		<td>Companies, agencies, institutions, etc.</td>
	</tr>
	<tr>
		<td>GPE</td>
		<td>Countries, cities, states.</td>
	</tr>
	<tr>
		<td>LOC</td>
		<td>Non-GPE locations, mountain ranges, bodies of water.</td>
	</tr>
	<tr>
		<td>PRODUCT</td>
		<td>Objects, vehicles, foods, etc. (Not services.)</td>
	</tr>
	<tr>
		<td>EVENT</td>
		<td>Named hurricanes, battles, wars, sports events, etc.</td>
	</tr>
	<tr>
		<td>WORK_OF_ART</td>
		<td>Titles of books, songs, etc.</td>
	</tr>
	<tr>
		<td>LAW</td>
		<td>Named documents made into laws</td>
	</tr>
	<tr>
		<td>LANGUAGE</td>
		<td>Any named language</td>
	</tr>
	<tr>
		<td>DATE</td>
		<td>Absolute or relative dates or periods.</td>
	</tr>
	<tr>
		<td>TIME</td>
		<td>Times smaller than a day.</td>
	</tr>
	<tr>
		<td>PERCENT</td>
		<td>Percentage, including ”%“.</td>
	</tr>
	<tr>
		<td>MONEY</td>
		<td>Monetary values, including unit.</td>
	</tr>
	<tr>
		<td>QUANTITY</td>
		<td>Measurements, as of weight or distance.</td>
	</tr>
	<tr>
		<td>ORDINAL</td>
		<td>“first”, “second”, etc.</td>
	</tr>
	<tr>
		<td>CARDINAL</td>
		<td>Numerals that do not fall under another type</td>
	</tr>
	
</table>

example:
<host>/nlp/EntityRecognizer/all/The Wildlife Protection Act, 1972 is an Act of the Parliament of India enacted for protection of plants and animal species
	
	

