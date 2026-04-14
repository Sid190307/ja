interface playable{
void play();
void pause();
}

class musicplayer implements playable{
@Override
public void play(){
System.out.println("Playing Music...."); 
}

@Override
public void pause(){
System.out.println("Music paused...."); 
}
}

class videoplayer implements playable{
@Override
public void play(){
System.out.println("Playing Video...."); 
}

@Override
public void pause(){
System.out.println("Video paused...."); 
}
}

public class pro6{
public static void main(String args[]){
musicplayer  m = new musicplayer();
videoplayer v = new videoplayer();
m.play();
m.pause();
v.play();
v.pause();
}
}
