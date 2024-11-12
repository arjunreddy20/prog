const product = (a,b) => console.log(a*b)
product(5,10)

const student = {
    name: 'John',
    age:22,
    address: "hyderbad",
    greet() {
        console.log("Hello " + this.name)
    }
}
student.greet()