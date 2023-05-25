//WHEN - Alternative to IF ELSE
fun main (){
    val marks :Int = 65
    when (marks){
        in 0 .. 30 ->{
            println("You scored $marks,Its a Fail")
        }
        in 31 .. 50 ->{
            println("You scored $marks,Its Average")
        }
        in 51 .. 70 -> {
            println("You scored $marks,Its above  Average")
            if(marks > 60){
                println("Proceed to Next Level")
            }
            else{
                println("Cannot proceed to Next Level")
            }
        }
        in 71 .. 100 -> {
            println("You scored $marks,Its Execellent")
        }
        else -> {
            println("Not Allowed")
        }
    }// end when
}//end main