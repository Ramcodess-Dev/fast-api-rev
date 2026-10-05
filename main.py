from fastapi import FastAPI, Request

from mockdata import products

from dtos import ProductDTO





app = FastAPI()

@app.get("/")
def home():
    return "welcome to fastapi rev"


# @app.get("/contact")
# def contact():
#     return "you can call me anytime !"
@app.get("/products")
def get_products():
    return products

#path params

@app.get("/product/{product_id}")
def get_one_product(product_id:int):

    
    for oneProduct in products:
        if oneProduct.get("id") == product_id:
            return oneProduct



    return{
        "error": "Product not found"
    } 
##query params

# @app.get("/greet")
# def greet_user(name:str):
#     return {
#         "greet" : f"hello {name} , how r u doingg!!?"
#     }


@app.get("/greet")
def greet_user(request:Request):
    query_params = dict(request.query_params)


    return {
        "greet" : f"hello {query_params.get("name")} , your age is {query_params.get("age")}"
    }

    ## diff type of http methods

@app.post("/create_product")
def create_product(product_data:ProductDTO):
    product_data = product_data.model_dump()
    products.append(product_data)


    return{"status": "product created successfully...", "data":products}


# @app.put(f"/update_product/{product_id}")

# def update_product(product_data:ProductDTO, product_id:int):

#     for index, oneProduct in enumerate(products):
#         print(oneProduct)


#     return {"status": "product created successfully...", }

@app.put("/update_product/{product_id}")
def update_product(product_id: int, product_data: ProductDTO):
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            products[index] = product_data.model_dump()
            return {"status": "product updated successfully"}

    return {"error": "Product not found"}


# @app.delete("/delete_product/{product_id}")
# def delete_product(product_id: int):
#     for index, oneProduct in enumerate(products):
#         if oneProduct.get("id") == product_id:
#             deleted_product = products.pop(index)

            
# return {"status": "product deleted successfully...", "product": deleted_product}


@app.delete("/delete_product/{product_id}")
def delete_product(product_id: int):
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            deleted_product = products.pop(index)
            return {
                "status": "product deleted successfully...",
                "product": deleted_product
            }

    return {
        "error": "Product not found"
    }


