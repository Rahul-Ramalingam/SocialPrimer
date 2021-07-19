


class SliderModel{

  String imageAssetPath;
  String title;
  String desc;

  SliderModel({this.imageAssetPath,this.title,this.desc});

  void setImageAssetPath(String getImageAssetPath){
    imageAssetPath = getImageAssetPath;
  }

  void setTitle(String getTitle){
    title = getTitle;
  }

  void setDesc(String getDesc){
    desc = getDesc;
  }

  String getImageAssetPath(){
    return imageAssetPath;
  }

  String getTitle(){
    return title;
  }

  String getDesc(){
    return desc;
  }

}


List<SliderModel> getSlides(){

  List<SliderModel> slides = new List<SliderModel>();
  SliderModel sliderModel = new SliderModel(); 
  
  sliderModel.setDesc("In the fight against the coronavirus, social distancing has proven to be a very effective measure to slow down the spread of the disease. While millions of people are staying at home to help flatten the curve, many of our customers in the manufacturing and pharmaceutical industries are still having to go to work every day to make sure our basic needs are met.To complement our customers’ efforts and to help ensure social distancing protocol in their workplace, Team AI Minds has developed an AI-enabled social distancing detection tool that can detect if people are keeping a safe distance from each other by analysing real time video streams from the camera.Our model also identifies crowd strength, by this people can avoid traveling to highly crowded areas to avoid the possible transmission of the deadly virus");
  sliderModel.setTitle("Product by Ai MinDs");
  sliderModel.setImageAssetPath("assets/logo.png");
  slides.add(sliderModel);


  sliderModel = new SliderModel(); 
  //1
  sliderModel.setDesc("Mentor");
  sliderModel.setTitle("T.Rajasekaran");
  sliderModel.setImageAssetPath("assets/Mr.T.Rajasekaran.jpg");
  slides.add(sliderModel);

  sliderModel = new SliderModel();

  //2
  sliderModel.setDesc("AI Model|UI Designer");
  sliderModel.setTitle("Rohith Raj.R");
  sliderModel.setImageAssetPath("assets/rohith.jpeg");
  slides.add(sliderModel);

  sliderModel = new SliderModel();

  //3
  sliderModel.setDesc("AI Model|App Developer");
  sliderModel.setTitle("R.Rahul");
  sliderModel.setImageAssetPath("assets/rahulr.jpg");
  slides.add(sliderModel);

  sliderModel = new SliderModel();
  sliderModel.setDesc("AI Model Developer");
  sliderModel.setTitle("M.Nishanth");
  sliderModel.setImageAssetPath("assets/nishanth.jpeg");
  slides.add(sliderModel);

  sliderModel = new SliderModel();
  sliderModel.setDesc("Full Stack Developer");
  sliderModel.setTitle("L.R.Vishnu Varthan");
  sliderModel.setImageAssetPath("assets/vishnu.jpeg");
  slides.add(sliderModel);

  sliderModel = new SliderModel();
  sliderModel.setDesc("Front-end Designer");
  sliderModel.setTitle("B.Rahul");
  sliderModel.setImageAssetPath("assets/rahulb.jpg");
  slides.add(sliderModel);

  sliderModel = new SliderModel();
  sliderModel.setDesc("Product|UI Designer");
  sliderModel.setTitle("Abhishek");
  sliderModel.setImageAssetPath("assets/abhishek.jpeg");
  slides.add(sliderModel);

  sliderModel = new SliderModel();
  sliderModel.setDesc("Product Designer");
  sliderModel.setTitle("Moulik");
  sliderModel.setImageAssetPath("assets/moulik.jpeg");
  slides.add(sliderModel);

  sliderModel = new SliderModel();
  sliderModel.setDesc("UI Designer");
  sliderModel.setTitle("chandhru");
  sliderModel.setImageAssetPath("assets/chandhru.jpeg");
  slides.add(sliderModel);

  sliderModel = new SliderModel();
  sliderModel.setImageAssetPath("assets/icon.jpg");
  slides.add(sliderModel);

  sliderModel = new SliderModel();

  return slides;
}