 (function() 
 {
  var allQuestions = [{
    question: "What would you choose ?",
    options: ["Instagram", "Reddit"],
    answer: 1
  }, {
    question: "What would you choose ?",
    options: ["Animated Classics", "Netflix Series"],
    answer: 0
  }, {
    question: "What would you choose ?",
    options: ["Start up", "Research"],
    answer: 1
  },{
    question: "If u were preparing for your final exams, what would you prefer ?",
    options: ["Books", "YouTube Videos"],
    answer: 0
  }, {
    question: "What would be your additional subject if choosing one was compulsary ?",
    options: ["English", "Economics"],
    answer: 1
  },{
    question: "If you were a UP resident and had 1 GB data, what would you do ?",
    options: ["Stream cricket", "Watch anime"],
    answer: 0
  },{
    question: "Can scientists turn into pickle anytime they want ?",
    options: ["Yes", "No"],
    answer: 0
  },{
    question: "Will you buy a N-word press for $10 ?",
    options: ["Sweet deal", "WTF is that?"],
    answer: 0
  },{
    question: "Do you tend to finish your assignments",
    options: ["At the 11th hour", "Hire someone to do it"],
    answer: 0
  },{
    question: "Does Gary Oldman shed feathers ?",
    options: ["Yes", "No"],
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
        var geeklink = document.createElement('a');
        geeklink.appendChild(document.createTextNode('Join Community')); 
        geeklink.setAttribute('href', 'http://google.com');
        var sslink = document.createElement('a');
        sslink.appendChild(document.createTextNode('Join Community')); 
        sslink.setAttribute('href', 'https://www.youtube.com/');   
        
        for (var i = 0; i < selectOptions.length; i++) 
        {
          if (selectOptions[i] === allQuestions[i].answer) 
          {
            correct++;
          }
        }
        score.append('Your psychometric score is ' + correct + ' out of ' +allQuestions.length);
       
          if (correct < 6) {
          text = "Yipee! Welcome to the community of Social Sapiens.Scroll a bit and Join the community by clicking on the below button : ";
          document.getElementById("demo").innerHTML = text;
         
          document.getElementById("yourgroup").value = "Social Sapiens";
            
              
        } else {
          text = "Bravo! Welcome to the community of Geek Clan.Scroll a bit and Join the community by clicking on the below button : ";
          document.getElementById("demo").innerHTML = text;
         
          document.getElementById("yourgroup").value = "Geek Clan";  
        }
           
        return score; 
        

        
  }
})();