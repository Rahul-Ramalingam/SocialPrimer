import 'package:flutter/material.dart';
import '../bloc.navigation_bloc/navigation_bloc.dart';
import 'package:sidebar_animation/data/data.dart';


class AboutPage extends StatefulWidget with NavigationStates {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<AboutPage> {

  List<SliderModel> mySLides = new List<SliderModel>();
  int slideIndex = 0;
  PageController controller;

  /*Widget _buildPageIndicator(bool isCurrentPage){
    return Container(
     margin: EdgeInsets.symmetric(horizontal: 2.0),
      height: isCurrentPage ? 10.0 : 6.0,
      width: isCurrentPage ? 10.0 : 6.0,
      decoration: BoxDecoration(
        color: isCurrentPage ? Colors.grey : Colors.grey[300],
        borderRadius: BorderRadius.circular(12),
      ),
    );
  }*/

  @override
  void initState() {
    super.initState();
    mySLides = getSlides();
    controller = new PageController();
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
          gradient: LinearGradient(
              colors: [const Color(0xff3C8CE7), const Color(0xff00EAFF)])),
      child: Scaffold(
        backgroundColor: Colors.white,
        body: Container(
          height: MediaQuery.of(context).size.height - 100,
          child: PageView(
            controller: controller,
              onPageChanged: (index) {
                setState(() {
                  slideIndex = index;
                });
              },
          children: <Widget>[
            SlideTile(
              imagePath: mySLides[0].getImageAssetPath(),
              title: mySLides[0].getTitle(),
              desc: mySLides[0].getDesc(),
            ),
            SlideTile(
              imagePath: mySLides[1].getImageAssetPath(),
              title: mySLides[1].getTitle(),
              desc: mySLides[1].getDesc(),
            ),
            SlideTile(
              imagePath: mySLides[2].getImageAssetPath(),
              title: mySLides[2].getTitle(),
              desc: mySLides[2].getDesc(),
            ),
            SlideTile(
              imagePath: mySLides[3].getImageAssetPath(),
              title: mySLides[3].getTitle(),
              desc: mySLides[3].getDesc(),
            ),
            SlideTile(
              imagePath: mySLides[4].getImageAssetPath(),
              title: mySLides[4].getTitle(),
              desc: mySLides[4].getDesc(),
            ),
            SlideTile(
              imagePath: mySLides[5].getImageAssetPath(),
              title: mySLides[5].getTitle(),
              desc: mySLides[5].getDesc(),
            ),
            SlideTile(
              imagePath: mySLides[6].getImageAssetPath(),
              title: mySLides[6].getTitle(),
              desc: mySLides[6].getDesc(),
            ),
            SlideTile(
              imagePath: mySLides[7].getImageAssetPath(),
              title: mySLides[7].getTitle(),
              desc: mySLides[7].getDesc(),
            ),
            SlideTile(
              imagePath: mySLides[8].getImageAssetPath(),
              title: mySLides[8].getTitle(),
              desc: mySLides[8].getDesc(),
            ),
            SlideTile(
              imagePath: mySLides[9].getImageAssetPath(),
              title: mySLides[9].getTitle(),
              desc: mySLides[9].getDesc(),
            ),

          ],
          ),),
    ));
  }
}

class SlideTile extends StatelessWidget {
  String imagePath, title, desc;

  SlideTile({this.imagePath, this.title, this.desc});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.symmetric(horizontal: 20),
      alignment: Alignment.center,
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          CircleAvatar(
            radius: (52),
            backgroundColor: Colors.white,
            child: ClipRRect(
              borderRadius:BorderRadius.circular(50),
              child: Image.asset(imagePath),
            )
        ),
          //Image.asset(imagePath),
          SizedBox(
            height: 40,
          ),
          Text(title, textAlign: TextAlign.center,style: TextStyle(
            fontWeight: FontWeight.w500,
            fontSize: 20
          ),),
          SizedBox(
            height: 20,
          ),
          Text(desc, textAlign: TextAlign.center,style: TextStyle(
          fontWeight: FontWeight.w500,
              fontSize: 14))
        ],
      ),
    );
  }
}


