fun main(){
    val amount:Short = 354
    if(amount > 34 && amount < 2500 ){
       println("Amount withdrawn $amount ,sh 25 will be deducted")
    }
    

    else if (amount in 2501 ..5000){
       println("Amount withdrawn $amount ,sh 65 will be deducted")
    }


    else if (amount in 5001 .. 10000){
       println(" Amount withdrawn $amount,sh 90 will be deducted")
    }


    else if (amount  in 10001.. 20000 ){
       println("Amount withdrawn $amount , sh 105 will be deducted")
    }


    else{
       println("$amount withdrawn")
    }

}//end main
