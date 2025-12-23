class Text
{
int a,b;
test(int i,int j)
{
a=i;b=j;
}
vode method1(test o)
{
a.o=o.a*2;
b.o=o.b/2;
}
}
public class PassobjRef
{
public static void main(String args[])
{
Test obj = new Test(15,20);
System.out.print("Before call"+obj.a+" "+obj.b);
obj.method1(obj);
System.out.print("After call"+obj.a+" "+obj.b);
}
}