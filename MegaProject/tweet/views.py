from django.shortcuts import render,get_object_or_404, redirect

from .models import Tweet
from .forms import Tweetform


# Create your views here.
def index(request):
    return render(request, "index.html")


def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {"tweets": tweets})


def tweet_create(request):
    print(request.method)
    if request.method =="POST":
        print(request.POST)
        form = Tweetform(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = Tweetform()
    print(form)
    return render(request, 'tweet_form.html', {"form": form})

def tweet_edit(request,tweet_id):
    print(tweet_id)
    tweet = get_object_or_404(Tweet,pk = tweet_id, user = request.user)
    print(tweet)
    print(request.method)
    if request.method =="POST":
        form = Tweetform(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form  =Tweetform(instance=tweet)
    return render(request, 'tweet_form.html', {"form": form})


def tweet_delete(request, tweet_id) :
    tweet= get_object_or_404 (Tweet, pk=tweet_id,user =request.user)
    print(tweet)
    print(request.method)
    if request.method =="POST":
        tweet.delete()
        return redirect( 'tweet_tist')
    return render(request, 'tweet_confirm_delete.html', {"tweet": tweet})
