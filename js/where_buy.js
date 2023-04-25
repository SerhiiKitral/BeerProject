const csvFilePath = '../database/ShopProducts.csv';

const beernameColumn = 'beername';
const volumeColumn = 'volume';
const urlColumn = 'url';
const priceColumn = 'price';
const shopColumn = 'shop';
const beertypeColumn = 'beertype';

let data = [];

Papa.parse(csvFilePath, {
    download: true,
    header: true,
    complete: function(results) {
        data = results.data;
        showResults();
    }
});

function autocompleteMatch(input) {
    if (input == '') {
        showResults();
    }
    const reg = new RegExp(input, 'i');
    return data.filter(function(row) {
    return row[beernameColumn] && row[beernameColumn].match(reg);
    }).map(function(row) {
    return { beername: row[beernameColumn], volume: row[volumeColumn], url: row[urlColumn], price: row[priceColumn], shop:row[shopColumn], beertype: row[beertypeColumn]  };
    });
}
function addCurrency(str) {
    if (str && str.endsWith('грн.')) {
        str = str.replace(' грн.', '₴');
    } else if (str) {
        str += '₴';
    }
    return str;
}
function addVolume(str) {
    if (str && !str.endsWith('Л')) {
        str += 'Л';
    }
    return str;
}
function showResults(val) {
    const name = document.getElementById("result");
    name.innerHTML = '';
    let list = '';
    const terms = autocompleteMatch(val);
    for (let i = 0; i < terms.length; i++) {
        let price = addCurrency(terms[i].price);
        let volume = addVolume(terms[i].volume);
        list +=
        '<a href="' + terms[i].url + '">' + 
            '<div id="left">' +
                '<div id="name">' + terms[i].beername + '</div>' + 
                '<div id="beertype">' + terms[i].beertype + '</div>' + 
                '<div id="shop">' + terms[i].shop + '</div>' + 
            '</div>' +
            '<div id="right">' +
                '<div id="volume">' + volume + '</div>' + 
                '<div id="price">' + price + '</div>' + 
            '</div>' +
        '</a>';
        }
    name.innerHTML = list;
}