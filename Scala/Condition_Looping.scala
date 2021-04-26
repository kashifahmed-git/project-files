class Condition_Looping
{

}
object Condition_Looping
{
  def main(args: Array[String])
  {
    /*
    var a = 10; val b=5;
    if(a>b){
        println("A is bigger !")
      }
    else if(a<b){
        println("B is bigger !")
      }
      else{
        println("A and B are equal")
      }
    */

   /*
    var a = 10;
    for(a <- 1 to 10 if 5/a==0)
    {
     println("a:"+a)
    }
      val out = for(a <- 1 to 10 if a%2==0) yield a
    print(out)

*/
 /*
   var a = 0;
    while(a<10)
      {
        var square = a*a
        println("The Square root of "+a+" is " +square)
        a=a+1
      }
*/
 println("Enter the number of tables")
 var table_no = scala.io.StdIn.readInt()
    var a= 1;

    while (a <= table_no )
      {
        println(+a+" tables")
          var i = 1
          while(i <= 10)
          {
            var result = a * i
            println(a +" x "+i+" = "+result)
            i=i+1
          }
        a=a+1

      }


  }
}