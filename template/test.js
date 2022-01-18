async function showMap(fileName){
  $.get(fileName), function(data) {
    for(let x = 0; x<362; x++){
      for (y = 0; y<181; y++){
        let res= y*362+x+1
          if (data[res] == "1") {
          ctx.fillRect(x, y, 1, 1);
          }
      }
    }
  }
}
