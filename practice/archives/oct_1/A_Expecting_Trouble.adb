with Ada.Text_IO;

procedure Main is
   S : String(1..51); -- You can adjust the size as needed
   P : Float;
   N : Natural;
   Ones : Natural := 0;
   Ps : Natural := 0;
begin
   -- Ada.Text_IO.Put("Enter a string: ");
   Ada.Text_IO.Get_Line(S, N);
   -- Ada.Text_IO.Put("Enter a floating-point number: ");
   Ada.Text_IO.Get(Item=>P);
   
   for I in 1 .. N loop
      if S(I) = '1' then
         Ones := Ones + 1;
      elsif S(I) = '?' then
         Ps := Ps + 1;
      end if;
   end loop;

   Ada.Text_IO.Put_Line(Float'Image((Ones + P * Float(Ps)) / Float(N)));
end Main;
