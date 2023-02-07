# Section D: Mentorship

This markdown file contains my responses to the Section D scenarios. I have selected to respond to **Option 2** as I am a Java fan and **Option 3** because people fascinate me.

## Option 2: Java Support Task

>In this task, we will simulate a typical interaction that you might have with a student during a mentor support call.
>The student asks you the following question:
"I am trying to do Task 6 and the JOptionPane.ShowDialog() does not work. For some reason it does not store the input to the string variable it is assigned to, so my do-while loop ends up in an infinite loop. Can you please help me?"

>Please describe the process that you would follow to help the student.


I tend to follow the following steps when a student approaches me with such a question:
1. What are their goals? What is the student trying to achieve? This can usually be obtained from a specification.
2. Understand the student's goal.
3. Get a reference point for the explanation I will use to assist the student. This reference point can be in my head, an actual piece of code, or an analogy or story I can use to get the student to understand where they are going wrong, and how to resolve their issue.
4. Ensure they understand my explanation and are satisfied. If they understand how to resolve their issue then I usually challenge them with a similar problem to ensure they truly understood the lesson. If they still do not understand where they are going wrong, I repeat *Step 3*. If they still do not understand where they are going wrong after repeating *Step 3* then I walk them through the solution to the problem step-by-step. The idea is to discuss the solution so that they can digest the small bites that make up the elephant(the solution), this can produce results in cases where a student is over-thinking things or struggling with confidence.

I apply the steps detailed above in the sections below.

### Step 1: The Goal
I find it best to have the student explain to me what they are trying to achieve. Once I have noted what they think the goal is, I read the specification document or question for myself. I do this because sometimes students read the question incorrectly or would have misunderstood a statement or word. Students can easily get tripped up by a term or concept that is foreign to them, in this case identifying the confusion is key to cracking the problem. If they are confused about something by clearing the confusion some students will be able to solve the problem.

In this case, though, the student seems to understand the goal, so on to *Step 2*.

### Step 2: Understand the Goal
This step is about me, I just make sure that I truly understand the goal. Reading parts of the specification or question again is important to ensure that I know all of the details. The last thing a confused student needs is a mentor/tutor that has misunderstood the question!

### Step 3: Reference Point
With User Interface problems the best reference point tends to be a code block. It allows me to quickly identify what is needed to answer the question. I have a lot of experience with *JavaFX* and *Swing* so I either write the code down, reference past code, or use Oracle documentation or a blog site like [GeeksforGeeks](https://www.geeksforgeeks.org/). The following is a reference point I believe is appropriate for this problem:
```
import javax.swing.JOptionPane;

public class Reference {

    public static void main(String[] args) {
        String m = JOptionPane.showInputDialog("How old are you?");
        System.out.println(m);
    }
}
```

### Step 4: Understanding
Now that I have my reference point I can start explaining how a *JOptionPane* Dialog window works. The student will then realise that they do not need a do-while loop and this gets rid of their infinite loop issue. They will also realise that they are using the wrong method and can use the **showInputDialog** method to obtain and store required the string input value from the User.

Usually, with User Interface problems the student will nod yes that they understand the explanation as the work tends to be about creating an object or calling the right method at the right time. There tends to be no underlying mathematical or statistical logic to understand. If they still do not understand my explanation(after repeating *Step 3* again), walking them through the solution tends to produce great results in this case.

When I am helping a student with such a problem I find it important to take a few minutes to discuss the bigger picture. Discussing how User Interfaces work in general can also help such a student. They will quickly learn that loops tend not to be necessary for most applications with User Interfaces as many applications follow a Model-view-controller pattern with program state changed by events triggered by keys, buttons, or the mouse.

Once the student is happy, it's good to challenge them with another similar problem like using *JOptionPane* methods like **showOptionDialog** or **showConfirmDialog**. Once they complete the new challenge I know that they have truly understood lesson.

## Option 3: Student Feedback

>Handling student concerns is an important part of the mentorship role. In the following scenario, you have provided feedback to a student in a code review for one of their submissions. After reading the feedback, the student responds in an irate manner claiming that you have provided feedback that does not provide any value, is generic and seems like you copy-pasted feedback just to complete the review. You did in fact provide non-generic, personalised and actionable feedback. On top of this, the student has also made a complaint on social media about the poor quality of your review.

> Please explain how you would handle this situation.


Interestingly enough, I have been in such a situation, except the negative '*post*' was made on a residence WhatsApp group chat. At this time I was a Student Leader(the Head Student) at Huis de Villiers residence at Stellenbosch University, and a student sent messages insulting my team's leadership due to our unwillingness to break strict University stipulated COVID-19 protocols. What I have found from such experiences is that people just want to be heard and want to see some action so the following steps tend to be appropriate to follow:
1. *Breathe in. Breathe out.* One must stay calm in such situations to ensure that emotions do not take over the situation and make things worse.
2. Difficult as it may be, emphasise, put yourself in their shoes, and try to understand their experience. Consider that they may be having a bad day, a loved one may have passed away, or they have put their everything into learning programming and are still not able to complete course projects and questions. The latter is common, I have seen so many smart students while at University studying difficult programmes like Actuarial Science or Engineering struggle with programming courses. Taking a moment to do this will make it easier to respond to them calmly, thoughtfully, and professionally. And emphasise is the keyword, not sympathise, I find that no matter the situation or person, I can always emphasise as I know that life can be hard. Sympathy on the other hand can feel impossible in some cases, especially in an era where the Internet is full of trolls.
3. I found from experience having a one-on-one chat with someone always does the trick. It's easier to understand each other and get to the roots of the problem, especially in this case where the negative review is unfounded. Honest and thoughtful responses tend to help get the person's guard down and get them to align with reality. I also find that it's easier to get the right tone of voice when responding to someone when in person, online people place a tone on your responses based on how they feel about you or the situation. If they are angry, they may read your online responses as if you are being rude or snarky. A video call can be used to achieve the desired result.
4. Ensure that your responses are honest and thoughtful. By the end of the day, this is one of your student's so focus on having an honest conversation about the situation. Ask questions and try to have them speak more than you so that they feel heard. Carefully worded questions can help lower someone's guard and get to the core of their grievances so that they can be resolved. Asking questions about the review you provided, areas that are unclear, and things they are struggling with can be a great starting point. It's important that the person feels that you care about their opinions and truly want to address their grievances. It helps to have a list of actions you are going to take and provide a timeline for those actions.
5. Respond to the student as quickly as possible, they will likely not expect such a swift response so this can help limit the damage.
6. Once the student is happy and feels their grievances have been resolved, ask them to remove or update their social media post.

With this said my tutor experience has taught me that some students want you to do the bulk of the work for them. Unfortunately, this can happen, in this case, an action-oriented approach is key to resolving the student's grievances. Such students tend not to be satisfied until some actions have been taken on their behalf. This can include a full discussion of the points in the review, almost like a live review, and sharing resources to help them with problem areas, videos especially tend to do the trick here.
