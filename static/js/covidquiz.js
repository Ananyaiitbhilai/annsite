(function() 
{
 var allQuestions = [{
   question: "Do vaccines cause autism ?",
   options: ["YES", "NO"],
   answer: 1
 }, {
   question: "Does RNA codes changes upon mutation in the COVID-18 virus cell ?",
   options: ["YES", "NO"],
   answer: 1
 }, {
   question: "Is the COVID vaccine RNA based ?",
   options: ["YES", "NO"],
   answer: 0
 },{
   question: "Are smokers more vulnerable to COVID-19 ?",
   options: ["YES", "NO"],
   answer: 0
 }, {
   question: "Which state is at the highest risk ?",
   options: ["UP", "MAHARASHTRA"],
   answer: 0
 },{
   question: "Are you certain that the person next to might not be infected ?",
   options: ["YES", "NO"],
   answer: 1
 },{
   question: "Do you keep a regular check on Covid Count, guidelines ?",
   options: ["YES", "NO"],
   answer: 0
 },{
   question: "Is COVID-19 susceptible to higher tempratures ?",
   options: ["YES", "NO"],
   answer: 0
 },{
   question: "Is the COVID immunity long term ?",
   options: ["YES", "NO"],
   answer: 1
 },{
   question: "Are weekly lockdowns a thing in India ?",
   options: ["YES", "NO"],
   answer: 0
   }];
  
  var quesCounter = 0;
  var selectOptions = [];
  var quizSpace = $('#quiz');
    
  nextQuestion();
    
  $('#next').click(function () 
    {
        chooseOption();
        if (isNaN(selectOptions[quesCounter])) 
        {
            alert('Please select an option !');
        } 
        else 
        {
          quesCounter++;
          nextQuestion();
        }
    });
  
  $('#prev').click(function () 
    {
        chooseOption();
        quesCounter--;
        nextQuestion();
    });
  
  function createElement(index) 
    {
        var element = $('<div>',{id: 'question'});
        var header = $('<h2>Question No. ' + (index + 1) + ' :</h2>');
        element.append(header);

        var question = $('<p>').append(allQuestions[index].question);
        element.append(question);

        var radio = radioButtons(index);
        element.append(radio);

        return element;
    }
  
  function radioButtons(index) 
    {
        var radioItems = $('<ul>');
        var item;
        var input = '';
        for (var i = 0; i < allQuestions[index].options.length; i++) {
          item = $('<li>');
          input = '<input type="radio" name="answer" value=' + i + ' />';
          input += allQuestions[index].options[i];
          item.append(input);
          radioItems.append(item);
        }
        return radioItems;
  }
  
  function chooseOption() 
    {
        selectOptions[quesCounter] = +$('input[name="answer"]:checked').val();
    }
   
  function nextQuestion() 
    {
        quizSpace.fadeOut(function() 
            {
              $('#question').remove();
              if(quesCounter < allQuestions.length)
                {
                    var nextQuestion = createElement(quesCounter);
                    quizSpace.append(nextQuestion).fadeIn();
                    if (!(isNaN(selectOptions[quesCounter]))) 
                    {
                      $('input[value='+selectOptions[quesCounter]+']').prop('checked', true);
                    }
                    if(quesCounter === 1)
                    {
                      $('#prev').show();
                    } 
                    else if(quesCounter === 0)
                    {
                      $('#prev').hide();
                      $('#next').show();
                    }
                }
              else 
                {
                    var scoreRslt = displayResult();
                    quizSpace.append(scoreRslt).fadeIn();
                    $('#next').hide();
                    $('#prev').hide();
                }
        });
    }
  
    function displayResult() 
    {
        var score = $('<p>',{id: 'question'});
        var correct = 0;
        var who = document.createElement('a');
        who.appendChild(document.createTextNode('BECOME COVID AWARE')); 
        who.setAttribute('href', 'https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public');
        var ls = document.createElement('a');
        ls.appendChild(document.createTextNode('BECOME COVID AWARE')); 
        ls.setAttribute('href', 'https://www.mohfw.gov.in/'); 
        
    
        
        for (var i = 0; i < selectOptions.length; i++) 
        {
          if (selectOptions[i] === allQuestions[i].answer) 
          {
            correct++;
          }
        }
        score.append('You scored ' + correct + ' out of ' +allQuestions.length);
       
          if (correct < 6) {
          text = "Sad, You are not much aware about COVID. Go and check out this necessary COVID information now. This might help world to combat COVID : ";
          document.getElementById("demo").innerHTML = text;
          document.getElementById('demo').appendChild(who);
          
            
              
        } else if (correct > 5 & correct < 9){
          text = "Good, You are aware about COVID but still awareness is needed. Go and Check out the live stats on COVID count now. This might help world to combat COVID in a better way : ";
          document.getElementById("demo").innerHTML = text;
          document.getElementById('demo').appendChild(ls);
         
        } else {
            text = "Bravo! you are very much aware about covid. But still you can check out live stats, link to it is provided on our home page."
            document.getElementById("demo").innerHTML = text;
           
          
        }
           
        return score;  
        

        
  }
})();
