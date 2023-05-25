fun main(){
    val  amount : Int = 5000
    when (amount){
        in 0.. 5900 ->{
            println(" Gross income $amount,Your Monthly Contribution will be sh 150")
        }
        in 6000 .. 7999 ->{
            println("Gross icome $amount, Your Montly Contribution will be sh 300 ")
        }
        in 8000 .. 11999 ->{
            println("Gross income $amount,Your Monthly Contribution will be sh 400")
        }
        in 12000 .. 14999 ->{
            println("Gross income $amount,Your Monthly Contribution will be sh 500 ")
        }
        in 15000 .. 19999 ->{
            println("Gros income $amount,Yoiur Monthly Contribution will be sh 600")
        }
        in 20000 .. 24999 ->{
            println("Gross income $amount,Your Monthly Contribution will be sh 750")
        }
        in 25000 .. 29999 ->{
            println("Gross income $amount,Your Monthly Contribution will be sh 850")
        }
        in 30000 .. 49999 ->{
            println("Gross income $amount,Your Monthly Contribution will be sh 1000")
        }
        in 50000 .. 99999 ->{
            println("Gross income $amount,Your Monthly Contribution wil be sh 1500 ")
        }
        else  -> {
            if(amount <0){
                println("Gross income $amount ,Negative")
            }
            else{
            println("Gross income $amount,YOur Monthly Contribution will be sh 2500")
            }
        }


    }  
}