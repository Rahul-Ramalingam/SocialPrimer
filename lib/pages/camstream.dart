import 'package:flutter/material.dart';
import 'package:flutter_vlc_player/flutter_vlc_player.dart';
import 'package:flutter_vlc_player/vlc_player.dart';
import 'package:flutter_vlc_player/vlc_player_controller.dart';




class VideoPage1 extends StatefulWidget {
  VideoPage1({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<VideoPage1> {
  String _streamUrl;
  VlcPlayerController _vlcViewController;
  @override
  void initState() {
    super.initState();
    _vlcViewController = new VlcPlayerController();
  }

  void _incrementCounter() {
    setState(() {
      if (_streamUrl != null) {
        _streamUrl = null;
      } else {
        _streamUrl = 'http://192.168.1.4:8080/video';
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Streaming"),
        centerTitle: true,
        leading: IconButton(icon:Icon(Icons.arrow_back),
          onPressed:() => Navigator.pop(context, false),
      ),),
      body: Center(
        child: ListView(
          //mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            _streamUrl == null
                ? Container(
                    child: Center(
                      child: Text("Stream Closed")
                    ),
                  )
                : new VlcPlayer(
                    defaultHeight: 1920,
                    defaultWidth: 1080,
                    url: _streamUrl,
                    controller: _vlcViewController,
                    placeholder: InkWell(onTap: ()=>print("video tapped"),),
                  )
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Start streaming',
        child: Icon(_streamUrl == null ? Icons.play_arrow : Icons.pause),
      ),
    );
  }
}