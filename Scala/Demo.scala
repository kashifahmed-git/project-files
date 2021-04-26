class Demo
{
    def Add(x: Int, y: Int)
    {
      val z = x + y
      print("Added value is " + z)

    }

}

object Demo
{
  def main(args: Array[String])
  {
    var a = scala.io.StdIn.readInt()
    var b = scala.io.StdIn.readInt()

    var obj = new Demo();
    obj.Add(a,b)
  }
}
