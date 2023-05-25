//Lets create a triangle object
class Triangle{


    //Data Members
    public val base :Double = 58.5
    public val height : Double = 50.6

    // Member functions
    public fun findArea(){
        val answer= 0.5 * base *height
        println("Area is $answer")
    }

    public fun findPerimeter(){
        val answer = (base+height)*2
        println("Perimeter is $answer")
    }
}//end  class


fun main (){
    val myObject = Triangle()
    myObject.findArea()
    myObject.findPerimeter()

}

