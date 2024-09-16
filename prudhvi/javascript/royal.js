// royal.js
var products = [
    { name: "Royal Enfield Classic 350", price: 2499, image: "classic350.jpg" },
    { name: "Royal Enfield Himalayan", price: 2450, image: "Royal-Enfield-Himalayan.jpg" },
    { name: "Royal Enfield Hunter 350", price: 3400, image: "hunter350.png" },
    { name: "Royal Enfield Meteor", price: 3789, image: "metro.jpg" },
    { name: "Royal Enfield Short Gun 350", price: 2003, image: "shortgun350.png" },
    { name: "Royal Enfield Interceptor", price: 4568, image: "interceptor.jpg" },
    { name: "Royal Enfield Continental GT 650", price: 4567, image: "gt 650.jpg" },
    { name: "Royal Enfield Bullet 350", price: 1459, image: "bullet-350.jpg" }
];

function displayProducts(products) {
    var contentWrapper = document.getElementById('contentWrapper');
    contentWrapper.innerHTML = '';

    products.forEach(function(product) {
        var productSection = document.createElement('div');
        productSection.classList.add('product');

        var img = document.createElement('img');
        img.src = "images/" + product.image;
        img.alt = product.name + " - Royal Enfield";

        var h2 = document.createElement('h2');
        h2.textContent = product.name;

        var pPrice = document.createElement('p');
        pPrice.classList.add('price');
        pPrice.textContent = "$" + product.price;

        var btn = document.createElement('button');
        btn.textContent = "Add to Cart";
        btn.onclick = function() {
            alert("Added " + product.name + " to cart");
        };

        productSection.appendChild(img);
        productSection.appendChild(h2);
        productSection.appendChild(pPrice);
        productSection.appendChild(btn);

        contentWrapper.appendChild(productSection);
    });
}

function searchProducts() {
    var searchTerm = document.getElementById('searchInput').value.toLowerCase();
    var searchResults = [];

    products.forEach(function(product) {
        if (product.name.toLowerCase().includes(searchTerm)) {
            searchResults.push(product);
        }
    });

    displayProducts(searchResults);
}

function sortByName() {
    products.sort(function(a, b) {
        return a.name.localeCompare(b.name);
    });

    displayProducts(products);
}

function sortByPrice() {
    products.sort(function(a, b) {
        return a.price - b.price;
    });

    displayProducts(products);
}

function toggleDropdown() {
    var menu = document.getElementById('dropdownMenu');
    menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
}

document.addEventListener('DOMContentLoaded', function() {
    displayProducts(products);
});
