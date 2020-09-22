#status.py

cl.send("""<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8"> 
	<title>智能停车系统 - 查询车位</title> 
	<link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css">  
	<script src="https://cdn.staticfile.org/jquery/2.1.1/jquery.min.js"></script>
	<script src="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>""");

btn_state = ['btn-success','btn-success','btn-success','btn-success','btn-success','btn-success','btn-success']
for i in range(1,7):
  if (park_slot[i] == True):
    btn_state[i] = 'btn-danger'
    
cl.send("""<div class="container">
	<div class="row clearfix">
		<div class="col-md-5 column">""");
cl.send("""			 <button type="button" class="btn btn-block btn-lg """ + btn_state[1] + """">车位1</button>""");
cl.send("""			 <button type="button" class="btn btn-block btn-lg """ + btn_state[2] + """">车位2</button>""");
cl.send("""			 <button type="button" class="btn btn-block btn-lg """ + btn_state[3] + """">车位3</button>""");
cl.send("""		</div>
		<div class="col-md-2 column">
			<h2 class="text-center"><strong>过道</strong></h2>
		</div>
		<div class="col-md-5 column">""");
cl.send("""			 <button type="button" class="btn btn-block btn-lg """ + btn_state[4] + """">车位4</button>""");
cl.send("""			 <button type="button" class="btn btn-block btn-lg """ + btn_state[5] + """">车位5</button>""");
cl.send("""			 <button type="button" class="btn btn-block btn-lg """ + btn_state[6] + """">车位6</button>""");
cl.send("""		</div>
	</div>
</div>
</body>
</html>""");

