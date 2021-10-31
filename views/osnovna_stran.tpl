  <h1>Didžeridu</h1>
  <hr>
  <blockquote>
    Tvoj najljubši program za beleženje zgodovine poslušanja. :)
  </blockquote>

  <form action="/nov-vnos/" method="POST">
    Izvajalec: <input type="text" name="izvajalec"><br>
    Album: <input type="text" name="album"><br>
    Žanri: <input type="checkbox" name="Rock">
           <label for="Rock"> Rock</label><br>
           <input type="checkbox" name="Metal">
           <label for="Metal"> Metal</label><br>
           <input type="checkbox" name="Folk">
           <label for="Folk"> Folk</label><br>
           <input type="checkbox" name="Hip hop">
           <label for="Hip hop"> Hip hop</label><br>
           <input type="checkbox" name="Alternativa">
           <label for="Alternativa"> Alternativa</label><br>
           <input type="checkbox" name="Pop">
           <label for="Pop"> Pop</label><br>
           <input type="checkbox" name="Eksperimentalna">
           <label for="Eksperimentalna"> Eksperimentalna</label><br>
           <input type="checkbox" name="Jazz">
           <label for="Jazz"> Jazz</label><br>
           <input type="checkbox" name="R&B">
           <label for="R&B"> R&B</label><br>
           <input type="checkbox" name="Klasična">
           <label for="Klasična"> Klasična</label><br>
           <input type="checkbox" name="Blues">
           <label for="Blues"> Blues</label><br>
           <input type="checkbox" name="Elektronska">
           <label for="Elektronska"> Elektronska</label><br>
           <input type="checkbox" name="Plesna">
           <label for="Plesna"> Plesna</label><br>
           <input type="checkbox" name="Punk">
           <label for="Punk"> Punk</label><br>
           <input type="checkbox" name="Govorjena beseda">
           <label for="Govorjena beseda"> Govorjena beseda</label><br>
           <input type="checkbox" name="Drugo">
           <label for="Drugo"> Drugo</label><br>
    Leto izida: <input type="text" name="leto izida">
  <input type="submit" value="Dodaj!">
  </form>

  <form action="/seznam-vnosov/" method="GET">
    <button type="submit">Prikaži pretekle vnose</button>
  </form>
