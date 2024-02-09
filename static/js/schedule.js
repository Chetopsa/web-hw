let table = document.getElementById('table2');
let big_image = document.getElementById('image_block');
let clock_element =  document.getElementById('clock_widget');


const images = new Map([
["anderson",'"/img/anderson.jpg" alt= "Anderson"'], ["nicholson", '"/img/Nicholson.jpg" alt="Nicholson"'],
["wiley",'"/img/Wiley.jpg" alt= "Wiley"'], ["akerman", '"/img/Akerman.jpg" alt= "Akerman"'], ["civil", '"/img/Civil_Engineering.jpg" alt= "Civil_Engineering"'],
["bio", '"/img/Molecular_Biology.jpg" alt= "Molecular_Biology"'], ["walter", '"/img/walter.jpg" alt= "Walter"']
]);
//returns the key for the map given the images row
function getImage(row){
    if(row == 1 || row == 5){
        return "anderson";
    }
    else if(row == 2 || row == 6){
        return "nicholson";
    }
    else if(row == 3 || row == 9){
        return "wiley";
    }
    else if(row == 4 || row == 10){
        return "akerman";
    }
    else if(row == 7){
        return "civil";
    }
    else if(row == 8){
        return "bio";
    }
    else{
        return "walter";
    }
}
function addImageToCell(event){
    let row = event.target.closest('tr');

    if(row && row.rowIndex > 0){
        let img_cell = row.cells[3];
        let img_string = images.get(getImage(row.rowIndex));
        if (!img_cell.getAttribute('data-original-content')) {
            img_cell.setAttribute('data-original-content', img_cell.innerHTML);
        }
        console.log(img_string);
        
        row.style.background = "grey";
        img_cell.innerHTML += '<br><img id="thumbnail" src='+ img_string+'>';
        big_image.innerHTML = '<img id="bigger_image" src='+ img_string+'>';

    }
}
function removeImageFromCell(event){
    let row = event.target.closest('tr');
    if(row && row.rowIndex > 0){
        let img_cell = row.cells[3];
        if (img_cell.getAttribute('data-original-content')) {
            img_cell.innerHTML = img_cell.getAttribute('data-original-content');
            img_cell.removeAttribute('data-original-content');
        }
        if (row.rowIndex % 2 == 0){
            row.style.background = "white";
        }
        else{
            row.style.background = "#f2f2f2";
        }
        // big_image.innerHTML = '<img id="bigger_image" src="/img/gophers-mascot.png" alt="pic of building"></img>';
    }
}
function updateClock(element){
    let clock = new Date();
    element.innerHTML += "<table><tr><td>"+clock.getHours()+"</td><td>"+clock.getMinutes()+"</td><td>"+clock.getSeconds+"</td></tr></table>";
}
table.addEventListener('mouseover', addImageToCell);
table.addEventListener('mouseout', removeImageFromCell);
console.log("hello\n");