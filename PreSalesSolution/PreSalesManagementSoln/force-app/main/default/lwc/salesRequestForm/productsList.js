import SalesRequestForm from "./salesRequestForm";

export class ProductSelector {
    constructor (parentObj) {
        this.parent = parentObj

        this.getProducts()

        if(!(this.parent instanceof SalesRequestForm))
            throw new Error('ProductSelector was invoked by an invalid parent')
    }

    products = []

    getProducts = () => {
        fetch(this.parent.url + 'products/')
            .then(res => res.json())
            .then(data => {this.products = data})
    }

    //search for products in the text bar
    searchEvt = (evt) => {
        const value = evt.target.value;
        if (value === '') {
            this.parent.filteredProducts = [];
            this.parent.searchBarEmpty = true

        } else {
            const lValue = value.toLowerCase();
            this.parent.filteredProducts = this.products.filter(item => item.name.toLowerCase().includes(lValue));
            this.parent.searchBarEmpty = false || !this.parent.filteredProducts.length
        }
    }

    //event button to add to cart
    addProd = (evt) => {
        const prod = evt.target.value;

        if (this.parent.selectedProducts.includes(prod))
            return;

        this.parent.selectedProducts.push(prod);
        this.products = this.products.filter(item => item.product_ID !== prod.product_ID);
        
        this.parent.template.querySelector(".search").value = '';
        this.searchEvt({target:{value: ''}})

        this.parent.setDisableButton()
    }

    //event button to remove from cart
    removeProd = (evt) => {
        const product_ID = parseInt(evt.target.dataset.item, 10)
        const product = this.parent.selectedProducts.find(item => item.product_ID === product_ID)

        this.products.push(product);
        this.parent.selectedProducts = this.parent.selectedProducts.filter(item => item !== product);

        this.parent.template.querySelector(".search").value = '';
        this.searchEvt({target:{value: ''}})

        this.parent.setDisableButton()
    }
}