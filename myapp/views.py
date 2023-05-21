from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from pprint import pprint
from Questgen import main
import nltk
nltk.download('stopwords')

'''
    1.Generate boolean (Yes/No) Questions.
    2.Generate MCQ Questions.
    3.Generate FAQ Questions.
    4.Paraphrasing Questions.
    5.Question Answering (Simple)'''

class Questions(ViewSet):
    def create(self,request):
        quetion_type_no = request.data.get('quetion_type_no')
        if not quetion_type_no:
                return Response({'message': 'Please enter quetion_type_no'}, 
                status=status.HTTP_400_BAD_REQUEST)
        
        content = request.data.get('content')
        if not quetion_type_no == "5":
            if not content:
                    return Response({'message': "Please enter content"}, 
                    status=status.HTTP_400_BAD_REQUEST)
            

        payload = {
                    "input_text": content
                }

        #1.Generate boolean (Yes/No) Questions.
        if quetion_type_no == "1":
            print("11111111111111111111111111111")
            qe= main.BoolQGen()
            output = qe.predict_boolq(payload)
            if output:
                return JsonResponse({
                        'status_code': status.HTTP_200_OK,
                        'message': 'successfull',
                        'data': output,
                    }, status=status.HTTP_200_OK)

            else:
                return Response({'status':status.HTTP_400_BAD_REQUEST,
                                'message':'something went wrong'
                                },status=status.HTTP_400_BAD_REQUEST)

        
        #2.Generate MCQ Questions.
        if quetion_type_no == "2":
            print('222222222222222222222222222222222')
            qg = main.QGen()
            output = qg.predict_mcq(payload)
            if output:
                return JsonResponse({
                        'status_code': status.HTTP_200_OK,
                        'message': 'successfull',
                        'data': output,
                    }, status=status.HTTP_200_OK)

            else:
                return Response({'status':status.HTTP_400_BAD_REQUEST,
                                'message':'something went wrong'
                                },status=status.HTTP_400_BAD_REQUEST)


        #3.Generate FAQ Questions.
        if quetion_type_no == "3":
            print('333333333333333333333333333333')
            qg = main.QGen()
            output = qg.predict_shortq(payload)
            if output:
                return JsonResponse({
                        'status_code': status.HTTP_200_OK,
                        'message': 'successfull',
                        'data': output,
                    }, status=status.HTTP_200_OK)

            else:
                return Response({'status':status.HTTP_400_BAD_REQUEST,
                                'message':'something went wrong'
                                },status=status.HTTP_400_BAD_REQUEST)


        #4.Paraphrasing Questions.
        if quetion_type_no == "4":
            print('444444444444444444444444444444')
            # content2 = request.data.get('content2')
            # if not content2:
            #         return Response({'message': "Please enter content2 for Paraphrasing Questions"}, 
            #         status=status.HTTP_400_BAD_REQUEST)
            
            qg = main.QGen()

            payload2 = {
            "input_text" : content,
            "max_questions": 5
            }
            output = qg.paraphrase(payload2)
            if output:
                return JsonResponse({
                        'status_code': status.HTTP_200_OK,
                        'message': 'successfull',
                        'data': output,
                    }, status=status.HTTP_200_OK)

            else:
                return Response({'status':status.HTTP_400_BAD_REQUEST,
                                'message':'something went wrong'
                                },status=status.HTTP_400_BAD_REQUEST)



        #5 Question Answering (Simple)
        if quetion_type_no == "5":
            print("555555555555555555555555555555555")
            answer = main.AnswerPredictor()
            question = request.data.get('question')
        
            if not question:
                return Response({'message': "Please enter question"}, 
                status=status.HTTP_400_BAD_REQUEST)

            answers = request.data.get('answers')
            if not answers:
                return Response({'message': "Please enter answers"}, 
                status=status.HTTP_400_BAD_REQUEST)
                
            payload3 = {
                "input_text" : answers,
                "input_question" : question
            }
            output = answer.predict_answer(payload3)
            if output:
                return JsonResponse({
                        'status_code': status.HTTP_200_OK,
                        'message': 'successfull',
                        'data': output,
                    }, status=status.HTTP_200_OK)

            else:
                return Response({'status':status.HTTP_400_BAD_REQUEST,
                                'message':'something went wrong'
                                },status=status.HTTP_400_BAD_REQUEST)




        #Question Answering (Boolean)
        if quetion_type_no == "6":
            print("6666666666666666666666666666666")
            question = request.data.get('question')
            if not question:
                return Response({'message': "Please enter question"},

                status=status.HTTP_400_BAD_REQUEST)
            payload4 = {
            "input_text" :content,
            "input_question" : question
            }
            answer = main.AnswerPredictor()
            output = answer.predict_answer(payload4)
            if output:
                return JsonResponse({
                        'status_code': status.HTTP_200_OK,
                        'message': 'successfull',
                        'data': output,
                    }, status=status.HTTP_200_OK)

            else:
                return Response({'status':status.HTTP_400_BAD_REQUEST,
                                'message':'something went wrong'
                                },status=status.HTTP_400_BAD_REQUEST)


        return Response({'status':status.HTTP_400_BAD_REQUEST,
                                'message':'something went wrong'
                                },status=status.HTTP_400_BAD_REQUEST)

