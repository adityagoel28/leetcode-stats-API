<!-- # LeetCode Stats API -->
<h1 align="center" color="blue">LeetCode Stats API</h1>

<p align="center">
  <img src="https://img.shields.io/badge/GraphQl-E10098?style=for-the-badge&logo=graphql&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
</p>

<p align="center">
  <img src="https://pyheroku-badge.herokuapp.com/?app=leetcode-stats-api">
</p>


<!-- <a href="https://github.com/KnlnKS/leetcode-stats">
  <img alt="LeetCode Stat Card" src="https://intense-dawn-46595.herokuapp.com/a/adityag28/" width="400"/>
</a> -->

<!-- [![KnlnKS's LeetCode stats](https://leetcode-stats-six.vercel.app/api?username=KnlnKS)](https://github.com/KnlnKS/leetcode-stats) -->

Welcome to the Leetcode Statistics API repository!

This API allows you to easily access statistical data about users on Leetcode, a popular platform for preparing for technical interviews and honing coding skills. With this API, you can retrieve information such as a user's:
- Overall statistics (i.e. total number of solved problems, out of total problems on LeetCode)
- Statistics by difficulty level (e.g. number of easy, medium, and hard problems solved)

```diff
@@ Work In Progress - Data Visualisation and more @@
```

<!-- #### Work in progress
More work is to be done on this project. -->

# How to Use
To use the Leetcode Statistics API, simply follow these steps:
- Append your Leetcode username to the end of the URL http://34.93.126.129:8000/{username}/. For example, if your Leetcode username is adityag28, the URL you would use would be http://34.93.126.129:8000/adityag28.
- Simply use the URL anywhere.
- The API will return an image object containing your Leetcode statistics which you can add anywhere in your portfolio or in your GitHub profile readme.

It's that easy! No need to worry about obtaining an API key or rate limiting - just make the request(use the URL) and get your stats.
I hope you find this API useful and appreciate any feedback you may have. Thank you for using the Leetcode Statistics API!

## Result
![image](http://34.93.126.129:8000/adityag28/)

The result will show the total number of questions on the LeetCode Platform, also with easy, medium and hard difficulty.
<br>
It will show the total number of questions solved by the user, and also show the individual questions solved by them based on the difficulty level.
<br>
With this data, you can get a sense of your progress and strengths on the Leetcode platform, as well as areas where you may want to focus your efforts.
## Theme
For users who prefer a darker visual theme, they can add `theme=dark` at the end. Right now only light and dark theme are only supported. In future more themes will be added.
For dark theme, use https://leetcode-stat-api.herokuapp.com/adityag28/theme=dark

## Result
![image](http://34.93.126.129:8000/adityag28/theme=dark)

## Usage
The most popular and common use for this API url is that the users can simply add this to their GitHub profile readme to showcase their LeetCode statistics, allowing others to easily view your progress and achievements on the Leetcode platform.

## Stargazers
[![Stargazers repo roster for @adityagoel28/leetcode-stats-API](https://reporoster.com/stars/adityagoel28/leetcode-stats-API)](https://github.com/adityagoel28/leetcode-stats-API/stargazers)
