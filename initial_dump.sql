--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.6
-- Dumped by pg_dump version 9.5.6

-- Started on 2017-04-12 01:24:10

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 1 (class 3079 OID 12355)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2102 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 181 (class 1259 OID 21965)
-- Name: speak; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE speak (
    speaker text NOT NULL,
    claim text NOT NULL,
    score double precision,
    trans_id text
);


ALTER TABLE speak OWNER TO postgres;

--
-- TOC entry 2094 (class 0 OID 21965)
-- Dependencies: 181
-- Data for Name: speak; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY speak (speaker, claim, score, trans_id) FROM stdin;
NIKKI HALEY	  This is CNN NEWSROOM, live from Los Angeles.	0.20699999999999999	1704/11/cnr.17
NIKKI HALEY	Ahead this hour: He promised America first but a new Trump doctrine could be emerging from the White House for Syria and North Korea.	0.27200000000000002	1704/11/cnr.17
NIKKI HALEY	And far-right French presidential candidate Marine Le Pen opened old wounds and outrages many with controversial comments about France's role in the Holocaust.	0.29199999999999998	1704/11/cnr.17
NIKKI HALEY	Plus a paying United Airlines customer roughed up and dragged off a plane that the company had overbooked shocking other passengers and airline travelers everywhere.	0.58099999999999996	1704/11/cnr.17
NIKKI HALEY	Hello and welcome to our viewers all around the world.	0.216	1704/11/cnr.17
NIKKI HALEY	I am Isha Sesay.	0.161	1704/11/cnr.17
NIKKI HALEY	NEWSROOM L.A. starts right now.	0.35499999999999998	1704/11/cnr.17
NIKKI HALEY	Well, Donald Trump is facing questions about what he'll do next regarding Syria but the U.S. President's top officials are sending mixed messages.	0.32300000000000001	1704/11/cnr.17
NIKKI HALEY	Some say Syrian President Bashar Assad has got to go, others say the U.S. is not looking for regime change.	0.26500000000000001	1704/11/cnr.17
NIKKI HALEY	So now, many are wondering after last week's strike in Syria, what exactly is Mr. Trump's foreign policy.	0.40699999999999997	1704/11/cnr.17
NIKKI HALEY	Here's CNN's Jim Sciutto.  	0.246	1704/11/cnr.17
DONALD TRUMP	  I ordered a targeted military strike on the air field in Syria from where the chemical attack was launched. 	0.5	1704/11/cnr.17
JIM SCIUTTO	  The world is a mess.	0.26300000000000001	1704/11/cnr.17
JIM SCIUTTO	I inherited a mess.	0.29199999999999998	1704/11/cnr.17
JIM SCIUTTO	Whether it's the Middle East, whether it's North Korea, whether it's so many other things. 	0.224	1704/11/cnr.17
JIM SCIUTTO	  So what is in effect the Trump Doctrine. 	0.219	1704/11/cnr.17
JOAN BISKUPIC	  We do what we can to make sure that our interests, both economically and national security, are at the forefront and we're not just going to become the world's policeman running around the world. 	0.21099999999999999	1704/11/cnr.17
JIM SCIUTTO	  Military action against one side of a war the U.S. has studiously avoided would seem to represent a shift from an isolationist America first strategy despite Trump's many assurances to the country. 	0.49199999999999999	1704/11/cnr.17
DONALD TRUMP	  I'm not, and I don't want to be the President of the world.	0.106	1704/11/cnr.17
DONALD TRUMP	I'm the President of the United States.	0.23400000000000001	1704/11/cnr.17
DONALD TRUMP	And from now on it's going to be America first. 	0.20599999999999999	1704/11/cnr.17
JIM SCIUTTO	  However, in the case of Syria, his administration is offering contradictory messages on whether the Syrian leader Bashar al-Assad must go. 	0.33800000000000002	1704/11/cnr.17
NIKKI HALEY	  Regime change is something that we think is going to happen because all of the parties are going to see that Assad is not the leader that needs to be taking place for Syria. 	0.20799999999999999	1704/11/cnr.17
REX TILLERSON	  Our priority in Syria, John, really hasn't changed.	0.26000000000000001	1704/11/cnr.17
REX TILLERSON	I think the President has been quite clear.	0.11899999999999999	1704/11/cnr.17
REX TILLERSON	First and foremost, we must defeat ISIS. 	0.29899999999999999	1704/11/cnr.17
JIM SCIUTTO	  Elsewhere, the next steps are equally unclear.	0.34100000000000003	1704/11/cnr.17
JIM SCIUTTO	In the battle against ISIS, there hasn't been much visible difference between President Trump and President Obama aside from some tough talk.	0.34999999999999998	1704/11/cnr.17
JIM SCIUTTO	The fact is the U.S. battle plan remains much the same.	0.318	1704/11/cnr.17
JIM SCIUTTO	A U.S.-led air campaign backed up by very limited U.S. forces on the ground, largely in support of Iraqi military and Syrian rebel forces.	0.50600000000000001	1704/11/cnr.17
JIM SCIUTTO	Again, despite Trump's frequent rhetoric to the contrary. 	0.20999999999999999	1704/11/cnr.17
DONALD TRUMP	  I would bomb the  out of them. 	0.20599999999999999	1704/11/cnr.17
JIM SCIUTTO	  In Asia, the Trump administration is making another show of force this week, diverting a U.S. carrier group to the Korean Peninsula following recent North Korean missile launches.	0.39600000000000002	1704/11/cnr.17
JIM SCIUTTO	However at Trump's meeting with the foreign leader most able to restrain Pyongyang, Chinese President Xi Jinping failed to produce a plan to deescalate tensions with the North Korean dictator Kim Jong- Un.	0.51000000000000001	1704/11/cnr.17
JIM SCIUTTO	Trump himself has often said that the difficulty in discerning his intensions is actually part of this plan. 	0.33000000000000002	1704/11/cnr.17
DONALD TRUMP	  I don't want people to figure me out.	0.10000000000000001	1704/11/cnr.17
DONALD TRUMP	I don't want people to know what my plan is.	0.096000000000000002	1704/11/cnr.17
DONALD TRUMP	I have plans.	0.23400000000000001	1704/11/cnr.17
DONALD TRUMP	I have plans but I don't want them to know what I'm thinking.	0.10000000000000001	1704/11/cnr.17
DONALD TRUMP	Does that make sense	0.19600000000000001	1704/11/cnr.17
JIM SCIUTTO	  Perhaps sensitive to public questions about how long- standing the effects of the U.S. military strike would be, the Defense Secretary James Mattis releasing a statement cataloguing the damage from U.S. cruise missiles including saying that some 20 percent of Syria's operational air force was taken out of commission permanently.	0.65600000000000003	1704/11/cnr.17
JIM SCIUTTO	Jim Sciutto, CNN -- Washington.  	0.219	1704/11/cnr.17
ISHA SESAY	  Well, joining me now in Los Angeles are talk radio host Mo Kelly, director of the USC School of International Relations Robert English and from Moscow, CNN's very own Paula Newton.	0.32700000000000001	1704/11/cnr.17
ISHA SESAY	Welcome to you all.	0.184	1704/11/cnr.17
ISHA SESAY	Robert English -- let's start with you.	0.214	1704/11/cnr.17
ISHA SESAY	[00:04:58] Irrespective of what the President and his people say, have last week's missile strikes committed this administration to a change of policy when it comes to Syria	0.39400000000000002	1704/11/cnr.17
ROBERT ENGLISH	  No, I don't think so.	0.055	1704/11/cnr.17
ROBERT ENGLISH	As we've seen, the strikes were limited.	0.254	1704/11/cnr.17
ROBERT ENGLISH	They were actually coordinated in advance in Russia to limit casualties and any possible greater in relations with Russia.	0.42099999999999999	1704/11/cnr.17
ROBERT ENGLISH	And in fact, they were considerably less than President Obama was proposing several years earlier in response to a similar outrage.	0.46600000000000003	1704/11/cnr.17
ROBERT ENGLISH	They're afraid, of course, of terrorist backlash as well.	0.20000000000000001	1704/11/cnr.17
ROBERT ENGLISH	So given the comments of Secretary Tillerson and others you can see that in fact there is some effort to gain maximum maneuverability in the American political context, right.	0.26400000000000001	1704/11/cnr.17
ROBERT ENGLISH	He's been praised for this.	0.27700000000000002	1704/11/cnr.17
ROBERT ENGLISH	He now has some maneuvering room with Russia instead of relentless criticism that he's Putin's puppet.	0.33700000000000002	1704/11/cnr.17
ROBERT ENGLISH	But in fact the damage to Russian relations, U.S.-Russian ties has been limited and there is space now to go into bargaining, to go into the meeting in Moscow later this week, you know, with some bargaining power, with some leverage. 	0.32100000000000001	1704/11/cnr.17
ISHA SESAY	  Let me follow up with you -- Robert.	0.21299999999999999	1704/11/cnr.17
ISHA SESAY	You talk about Secretary of State Tillerson's comment but he makes this comments where clearly he seems to be -- he's saying that the line we've heard to date of this country not wanting to wade into the situation in Syria, wanting to make ISIS the priority.	0.32300000000000001	1704/11/cnr.17
ISHA SESAY	But then you have the U.S. ambassador to the United Nations, Nikki Haley saying something entirely different.	0.27700000000000002	1704/11/cnr.17
ISHA SESAY	I mean how certain are we that there is a coherent policy within the administration when it comes to Syria. 	0.24099999999999999	1704/11/cnr.17
ROBERT ENGLISH	  Well, clearly there is some incoherence, right	0.107	1704/11/cnr.17
ISHA SESAY	  All right.	0.192	1704/11/cnr.17
ISHA SESAY	Mo Kelly -- to bring you in here.	0.184	1704/11/cnr.17
ISHA SESAY	Is this about the administration not wanting to telegraph where it stands when it comes to a policy on North Korea, the varying comments from Tillerson and Haley	0.17999999999999999	1704/11/cnr.17
MO KELLY	  If we use history as a guide, up until now they have never had a consistent unifying message as far foreign policy.	0.503	1704/11/cnr.17
MO KELLY	When I listen to Rex Tillerson or Nikki Haley, it seems like they're reading from different play books.	0.186	1704/11/cnr.17
MO KELLY	And I don't think that's their fault.	0.11	1704/11/cnr.17
MO KELLY	I think it starts from the top and they're not on the same page if only because they don't have a singular message which is being disseminated throughout all the ranks.	0.23400000000000001	1704/11/cnr.17
MO KELLY	And if we look at the specificity of the Syria strike, we have 59 Tomahawks which neither disabled nor deterred the enemy.	0.40100000000000002	1704/11/cnr.17
MO KELLY	So I would have to say that that was ineffective altogether. 	0.14699999999999999	1704/11/cnr.17
ISHA SESAY	  Let me go to Paula to pick up that point.	0.215	1704/11/cnr.17
ISHA SESAY	Paula -- we have seen jets take off from that very same airbase that was struck by those U.S. missiles.	0.29399999999999998	1704/11/cnr.17
ISHA SESAY	So you do have to wonder what the U.S. actually achieved with its actions with these strikes other than angering Russia. 	0.39200000000000002	1704/11/cnr.17
PAULA NEWTON	  Well, they certainly angered Russia.	0.22500000000000001	1704/11/cnr.17
PAULA NEWTON	As Rex Tillerson wakes up this morning here in Moscow he will expect to hear about this attack from the Russian government.	0.19400000000000001	1704/11/cnr.17
PAULA NEWTON	Having said that though, I think it does give some maneuverability here.	0.17499999999999999	1704/11/cnr.17
PAULA NEWTON	Remember this was short, sharp, it was measured and is something that Russia doesn't necessarily have to retaliate for.	0.33500000000000002	1704/11/cnr.17
PAULA NEWTON	And we have seen in fact quite a muted response from Russia despite all the rhetoric that's gone on in the last two days.	0.38500000000000001	1704/11/cnr.17
PAULA NEWTON	Sergey Lavrov, the foreign minister here and Rex Tillerson can have some constructive talks today when they meet in the next few hours.	0.32900000000000001	1704/11/cnr.17
PAULA NEWTON	And the reason is they're still trying to figure out what's exactly the U.S. policy is.	0.27100000000000002	1704/11/cnr.17
PAULA NEWTON	You know, everything we've been talking about here, the fact that there is no clear U.S. policy, in a way Rex Tillerson can use that to his advantage.	0.20200000000000001	1704/11/cnr.17
PAULA NEWTON	But what is key here, Isha, is that Tillerson comes to the table with some leverage.	0.193	1704/11/cnr.17
PAULA NEWTON	It will be interesting how far he tells the Russian government that the United States is willing to go if he can't seem to understand that look, the Russian government is either completely committed to keeping Assad in power or they are willing to help nudge him away from that regime and perhaps usher in a different political process in Syria. 	0.32400000000000001	1704/11/cnr.17
ISHA SESAY	  Robert English, to you -- the question of Assad's future.	0.17599999999999999	1704/11/cnr.17
ISHA SESAY	We had Nikki Haley talk about regime change in Syria being inevitable.	0.307	1704/11/cnr.17
ISHA SESAY	How do you see it	0.063	1704/11/cnr.17
ROBERT ENGLISH	  Look, it's over a year since Russia made clear that they're not wedded to Assad for the indefinite future.	0.35799999999999998	1704/11/cnr.17
ROBERT ENGLISH	It's a matter however of coordinating the transition and when Russians hear regime change, the term that Nikki Haley used, they think of Saddam Hussein's toppling in Iraq and the chaos that followed.	0.41299999999999998	1704/11/cnr.17
ROBERT ENGLISH	They think of the ousting of Muammar Gadhafi in Libya and the chaos that followed.	0.27200000000000002	1704/11/cnr.17
ROBERT ENGLISH	And what they'd rather see and what's frankly in our interest as well is coordination in, as you said, nudging him from power but having a plan in place for a transition government instead of the infighting sectarian ethnic and every other sort that would follow if he were just precipitously toppled as sometimes our comments suggest that we want to do. 	0.27200000000000002	1704/11/cnr.17
ISHA SESAY	  So you honestly believe that Russia's motivations here when it comes to not joining the U.S. position in terms of nudging Assad from power about maintaining peace in the region and preventing Syria from an all-out collapse as opposed to Russia expanding its sea of influence in Syria and the region	0.35699999999999998	1704/11/cnr.17
ROBERT ENGLISH	  I certainly think they want to maintain the influence they have which means that probably retention of rights at that naval base on the Mediterranean that they now enjoy would be an important part of Russia's demands in that transition.	0.17599999999999999	1704/11/cnr.17
ROBERT ENGLISH	But they have no love for Assad himself, absolutely none.	0.21199999999999999	1704/11/cnr.17
ROBERT ENGLISH	This is a cold-hearted, you know, practical calculation.	0.17199999999999999	1704/11/cnr.17
ROBERT ENGLISH	And Russia's interests will simply have to be taken into account in preventing the worst.	0.33800000000000002	1704/11/cnr.17
ROBERT ENGLISH	But expanding their influence, taking over the Middle East to dominate -- this is an exaggerated threat. 	0.20200000000000001	1704/11/cnr.17
ISHA SESAY	  Paula, to you there in Moscow, one consequence we have seen on the U.S. action is we've seen Russia and Iran publicly move closer together, both issuing their warning to the U.S. if they cross so- called red lines.	0.497	1704/11/cnr.17
ISHA SESAY	I mean, what could they be talking about in terms of a response	0.115	1704/11/cnr.17
PAULA NEWTON	  Well, I would think at this point not too seriously.	0.079000000000000001	1704/11/cnr.17
PAULA NEWTON	You know, that was very interesting that the Iranians and the Syrians have come out with that so-called red line.	0.251	1704/11/cnr.17
PAULA NEWTON	When we asked Dmitry Peskov, the Kremlin spokesperson about it he said, I have no idea what you're taking about.	0.34300000000000003	1704/11/cnr.17
PAULA NEWTON	Clearly as Robert was just saying, look, they continue to say our support for Assad is not unconditional.	0.27700000000000002	1704/11/cnr.17
PAULA NEWTON	You know, Isha -- they have that show of force.	0.155	1704/11/cnr.17
PAULA NEWTON	They have sent another warship back in the Mediterranean and as Robert pointed out, they have their seat at the table in the Middle East.	0.29399999999999998	1704/11/cnr.17
PAULA NEWTON	They fought hard on the battlefield.	0.216	1704/11/cnr.17
PAULA NEWTON	They've got their -- all their naval crew out there in the Mediterranean.	0.222	1704/11/cnr.17
PAULA NEWTON	It is one of the largest deployments of the military here in decades, probably going back to Cold War time.	0.41199999999999998	1704/11/cnr.17
PAULA NEWTON	They're not going to give that up easily.	0.191	1704/11/cnr.17
PAULA NEWTON	But does that mean they're really going to continue to support Assad	0.23000000000000001	1704/11/cnr.17
ISHA SESAY	  Robert English, Paula Newton -- my thanks to you both.	0.219	1704/11/cnr.17
ISHA SESAY	Mo Kelly -- stay with me.	0.182	1704/11/cnr.17
ISHA SESAY	I want to keep this conversation going.	0.10299999999999999	1704/11/cnr.17
ISHA SESAY	But my thanks to Robert and Paula -- appreciate it.	0.14899999999999999	1704/11/cnr.17
ISHA SESAY	North Korea is expected to hold a legislative gathering which can give us an idea of Pyongyang's agenda.	0.20799999999999999	1704/11/cnr.17
ISHA SESAY	The country is defiant after the U.S. redeployed warships for the Korean Peninsula.	0.39000000000000001	1704/11/cnr.17
ISHA SESAY	It's not an unusual military move by the U.S. but it's in response to North Korea's recent nuclear threat.	0.31	1704/11/cnr.17
ISHA SESAY	Here's the reaction from North Korea's government.	0.20399999999999999	1704/11/cnr.17
ISHA SESAY	Quote, "The Trump administration clamors about peace through strength and bring to the region of the Korean Peninsula a number of strategic weapons in order to frighten us.	0.33900000000000002	1704/11/cnr.17
ISHA SESAY	But we are not daunted even as to turn an eyelash.	0.25700000000000001	1704/11/cnr.17
ISHA SESAY	We'll make the U.S. fully accountable for catastrophic consequences that may be brought about by its high-handed and outrageous acts."	0.27700000000000002	1704/11/cnr.17
ISHA SESAY	Mo Kelly -- you're still with me.	0.23499999999999999	1704/11/cnr.17
ISHA SESAY	President Trump on the brink of getting sucked into Syria while at the same time facing a growing threat from North Korea, is it realistic to assume that this administration can hold to its America first doctrine. 	0.41899999999999998	1704/11/cnr.17
MO KELLY	  Well, they have to understand that making America first does include other nations around the world.	0.34999999999999998	1704/11/cnr.17
MO KELLY	I mean America first does extend to South Korea and our interests there.	0.26500000000000001	1704/11/cnr.17
MO KELLY	[00:15:01] And unfortunately, this President doesn't necessarily seem to realize that you don't have the luxury of only dealing with one nation at a time.	0.45300000000000001	1704/11/cnr.17
MO KELLY	He may think that he's only dealing with Syria but that also includes Russia and now it also includes North Korea.	0.31900000000000001	1704/11/cnr.17
MO KELLY	And also that was on -- at the same time dealing with the leader of China.	0.28399999999999997	1704/11/cnr.17
MO KELLY	All these things are coming together simultaneously.	0.21099999999999999	1704/11/cnr.17
MO KELLY	And we're not sure, at least I'm not sure whether President Trump with his strike in Syria was an addressing an audience of America to help his approval rating or whether he was actually trying to make a change in Syria and the Middle East because we know that that has not deterred al-Assad so at this point it stands (inaudible) that there's going to be an escalation.	0.44800000000000001	1704/11/cnr.17
MO KELLY	And an escalation in Syria means that there's going to be more of an impetus to have to deal with Russia and then also North Korea.	0.29299999999999998	1704/11/cnr.17
MO KELLY	I'm not so sure that the President has complete control of where this goes from here.	0.14000000000000001	1704/11/cnr.17
MO KELLY	And that concerns me greatly. 	0.17599999999999999	1704/11/cnr.17
ISHA SESAY	  It's interesting that you mentioned approval rating on the part of the President and the actions in Syria because what we know is that while the majority of American support for what happened, they're leery about going further about what comes next.	0.38500000000000001	1704/11/cnr.17
ISHA SESAY	And we also know that the President's own base, they feel like they didn't sign up for this.	0.25600000000000001	1704/11/cnr.17
ISHA SESAY	They didn't sign up for a president that was wading into Syria.	0.42399999999999999	1704/11/cnr.17
ISHA SESAY	I mean talk to me about the political cost, the risk for the President here. 	0.109	1704/11/cnr.17
MO KELLY	  It's very interesting because he received bilateral support from both Republicans and Democrats for at least doing something and that I guess served as a differentiation between him and President Obama who arguably did quote-unquote "nothing" in 2013.	0.40100000000000002	1704/11/cnr.17
MO KELLY	So he received bilateral support.	0.22600000000000001	1704/11/cnr.17
MO KELLY	But at the same time no one want so take this further than it needs to go.	0.11899999999999999	1704/11/cnr.17
MO KELLY	I mean we wanted to strike as a nation but we really didn't want to be tangled up in another Middle Eastern country.	0.29699999999999999	1704/11/cnr.17
MO KELLY	But unfortunately if you're going to get into a fight and you're not going to actually knock out the other guy, then you might as well stay around for the whole 12 rounds.	0.223	1704/11/cnr.17
MO KELLY	And I don't think America has the temerity or even the stomach for another long war in the Middle East.	0.16	1704/11/cnr.17
MO KELLY	But we may be on the precipice of that. 	0.17499999999999999	1704/11/cnr.17
ISHA SESAY	  Yes.	0.40600000000000003	1704/11/cnr.17
ISHA SESAY	We might indeed.	0.22700000000000001	1704/11/cnr.17
ISHA SESAY	Well, Mo Kelly -- I know you have the stomach to stick around for the next hour. 	0.19700000000000001	1704/11/cnr.17
MO KELLY	  Yes, ma'am. 	0.27500000000000002	1704/11/cnr.17
ISHA SESAY	  We'll keep this conversation going.	0.16900000000000001	1704/11/cnr.17
ISHA SESAY	Appreciate it.	0.21299999999999999	1704/11/cnr.17
ISHA SESAY	Thank you.	0.14799999999999999	1704/11/cnr.17
ISHA SESAY	Now, the U.S. Supreme Court is once again dominated by conservative justices.	0.29199999999999998	1704/11/cnr.17
ISHA SESAY	Neil Gorsuch took his judicial oath at the White House Monday and President Donald Trump celebrated his biggest political victory.	0.42499999999999999	1704/11/cnr.17
ISHA SESAY	Democrats fought an intense battle, you may remember, to block Gorsuch's confirmation.	0.221	1704/11/cnr.17
ISHA SESAY	Senate Republicans, well they changed those rules to end that blockade.	0.245	1704/11/cnr.17
ISHA SESAY	Gorsuch fills the vacancy left by Antonin Scalia's death nearly 14 months ago.  	0.42099999999999999	1704/11/cnr.17
JUSTICE NEIL GORSUCH	  I will never forget that to whom much is given, much will be expected.	0.30599999999999999	1704/11/cnr.17
JUSTICE NEIL GORSUCH	And I promise you that I will do all my powers permit to be a faithful servant of the Constitution and laws of this great nation.	0.214	1704/11/cnr.17
JUSTICE NEIL GORSUCH	Thank you.	0.14799999999999999	1704/11/cnr.17
JUSTICE NEIL GORSUCH	Let's bring in CNN Supreme Court analyst Joan Biskupic.	0.26000000000000001	1704/11/cnr.17
JUSTICE NEIL GORSUCH	She joins us now from Irvine, California.	0.20100000000000001	1704/11/cnr.17
JUSTICE NEIL GORSUCH	Thank you so much for being with us -- Joan.	0.161	1704/11/cnr.17
JUSTICE NEIL GORSUCH	So Judge Gorsuch is not Justice Gorsuch.	0.24399999999999999	1704/11/cnr.17
JUSTICE NEIL GORSUCH	How soon will we feel his impact on the court	0.081000000000000003	1704/11/cnr.17
JOAN BISKUPIC	  You know, on Thursday, he will vote in a private conference with the rest of the justices about some pending appeals.	0.252	1704/11/cnr.17
JOAN BISKUPIC	And then the following Monday we'll see the list of which cases they've taken in and rejected.	0.30399999999999999	1704/11/cnr.17
JOAN BISKUPIC	We wouldn't see his specific vote but his influence will be there.	0.14099999999999999	1704/11/cnr.17
JOAN BISKUPIC	So right away this week, he will start having an effect on the law of the land here.	0.26100000000000001	1704/11/cnr.17
JOAN BISKUPIC	And then what you'll see is, beginning the week of the 17th, the justices will be hearing oral arguments.	0.19400000000000001	1704/11/cnr.17
JOAN BISKUPIC	So we'll see him up there on that elevated bench in this new chair that has been made specifically for him and I'm sure he's going to jump in and with some questions and try to be a player.	0.22900000000000001	1704/11/cnr.17
JOAN BISKUPIC	So we'll see that.	0.16300000000000001	1704/11/cnr.17
JOAN BISKUPIC	And then, you know, June is right around the corner here and that's when all of our big rulings come.	0.20799999999999999	1704/11/cnr.17
JOAN BISKUPIC	And he will have a vote in all of these April sitting cases and then also orders.	0.28100000000000003	1704/11/cnr.17
JOAN BISKUPIC	You know, we've got the travel litigation percolating up.	0.313	1704/11/cnr.17
JOAN BISKUPIC	We have some other emergency matters percolating up that he'll have a hand in.	0.33500000000000002	1704/11/cnr.17
JOAN BISKUPIC	So I think it will be pretty quick that we'll see his influence. 	0.094	1704/11/cnr.17
ISHA SESAY	  As you mentioned the travel ban, let me pick up on that.	0.25600000000000001	1704/11/cnr.17
ISHA SESAY	You know, there are some out there who believe that this administration has purposely dragged its feet in terms of its actions in appealing the travel, you know, trying to untie it in its judicial wranglings because obviously the expectation is it will go to the Supreme court and they wanted to see Gorsuch on the bench when that happens.	0.29199999999999998	1704/11/cnr.17
ISHA SESAY	Do you believe from what we know of him that his being on the court means this will go the administration's way	0.087999999999999995	1704/11/cnr.17
JOAN BISKUPIC	  I think that the chances are that it will now go the administration's way.	0.182	1704/11/cnr.17
JOAN BISKUPIC	Now, there's so many different variables.	0.187	1704/11/cnr.17
JOAN BISKUPIC	So, you know, we're just speculating here.	0.108	1704/11/cnr.17
JOAN BISKUPIC	[00:20:02] But first of all he was chosen as a conservative.	0.502	1704/11/cnr.17
JOAN BISKUPIC	He was screened intensively by conservative groups here -- the Federalist Society and the Heritage Foundation.	0.28499999999999998	1704/11/cnr.17
JOAN BISKUPIC	He seems to have -- he seems to be quite compatible with President Trump's outlook on things.	0.23899999999999999	1704/11/cnr.17
JOAN BISKUPIC	We just don't know yet, you know, how much -- how much politics might be infecting his view and how much his general conservatism from a lower court will play out at the high court.	0.084000000000000005	1704/11/cnr.17
JOAN BISKUPIC	But definitely the chances of the administration succeeding at the Supreme Court have been increased by virtue of this new (inaudible) conservative.	0.44400000000000001	1704/11/cnr.17
JOAN BISKUPIC	So -- the other thing I would say about the lower court litigations so far it's been going against the administration.	0.27300000000000002	1704/11/cnr.17
JOAN BISKUPIC	But sometimes lower court judges themselves keep their eye on who's at the Supreme Court and what might happen.	0.161	1704/11/cnr.17
JOAN BISKUPIC	And until today that court was deadlocked, essential four-four with four liberals and four conservatives on many dilemmas.	0.377	1704/11/cnr.17
JOAN BISKUPIC	And I bet that that probably had an effect on some of the lower court judges in many areas.	0.30499999999999999	1704/11/cnr.17
JOAN BISKUPIC	But now there's a whole new team at the very top, essentially. 	0.20599999999999999	1704/11/cnr.17
ISHA SESAY	  You mean there's a whole new gang in town, so to speak.	0.151	1704/11/cnr.17
ISHA SESAY	Joan Biskupic -- appreciate it.	0.26000000000000001	1704/11/cnr.17
ISHA SESAY	Thank you so much for the insight. 	0.13	1704/11/cnr.17
JOAN BISKUPIC	  Sure. 	0.16400000000000001	1704/11/cnr.17
ISHA SESAY	  Time to take a quick break now.	0.222	1704/11/cnr.17
ISHA SESAY	Next on NEWSROOM L.A. people in California are mourning the victims of a shocking murder-suicide inside an elementary school.	0.32200000000000001	1704/11/cnr.17
ISHA SESAY	But how damaging have they been to her standing	0.051999999999999998	1704/11/cnr.17
ISHA SESAY	Plus shocking video of authorities roughing up a United Airlines customer -- the video is hard to watch -- you're seeing there being yanked off the plane.	0.40400000000000003	1704/11/cnr.17
ISHA SESAY	What other passengers are saying about the disturbing incident.	0.25700000000000001	1704/11/cnr.17
ISHA SESAY	We'll have that for you, next.  	0.255	1704/11/cnr.17
ISHA SESAY	  Well, an eight-year-old boy and his teacher had been killed in an elementary school shooting in California.	0.26900000000000002	1704/11/cnr.17
ISHA SESAY	Police say the gunman was targeting the teacher, his estranged wife, before killing himself.	0.27500000000000002	1704/11/cnr.17
ISHA SESAY	Another boy was injured though police say the children were not the target.	0.248	1704/11/cnr.17
ISHA SESAY	Stephanie Elam is in San Bernardino with more. 	0.32500000000000001	1704/11/cnr.17
STEPHANIE ELAM	  Isha -- this tragedy took place just before 10:30 in the morning on Monday.	0.35399999999999998	1704/11/cnr.17
STEPHANIE ELAM	And what we understand happened from police is that a 53-year-old man came to the elementary school here in San Bernardino, California, went to the front office, processed as anyone would be as a visitor to the school.	0.42099999999999999	1704/11/cnr.17
STEPHANIE ELAM	and then he walked to the classroom where his estranged wife -- they'd only been married for a couple of months, we understand -- was teaching her special needs class.	0.312	1704/11/cnr.17
STEPHANIE ELAM	It's a class made up of first through fourth graders.	0.38700000000000001	1704/11/cnr.17
STEPHANIE ELAM	[00:24:59] Police say he walked in and without any announcement began shooting at his estranged wife, killing her -- her name being Karen Smith (ph).	0.56200000000000006	1704/11/cnr.17
STEPHANIE ELAM	Karen Smith was there teaching and standing behind her were two boys, a nine-year-old boy who we understand is in stable condition; and an eight-year-old boy who understand has succumbed to his gunshot wounds.	0.314	1704/11/cnr.17
STEPHANIE ELAM	That eight-year-old boy's name is Jonathan Martinez.	0.153	1704/11/cnr.17
STEPHANIE ELAM	Then after this all transpiring, they say that the man then turned the gun on himself, killing himself.	0.248	1704/11/cnr.17
STEPHANIE ELAM	So they do believe it was a murder- suicide here inside the school.	0.16600000000000001	1704/11/cnr.17
STEPHANIE ELAM	Officials working very quickly to reunite the children in that classroom with their parents quickly.	0.16900000000000001	1704/11/cnr.17
STEPHANIE ELAM	The rest of the school of about 500 students, they worked methodically to reunite those children with their parents after making sure they were releasing them to their legal guardians.	0.41699999999999998	1704/11/cnr.17
STEPHANIE ELAM	But all in all, it just (ph) was to be a very tragic development here in San Bernardino, California -- Isha.  	0.17100000000000001	1704/11/cnr.17
ISHA SESAY	 Our thanks to Stephanie Elam for that.	0.17599999999999999	1704/11/cnr.17
ISHA SESAY	Just ahead on CNN NEWSROOM, opening old wounds.	0.19400000000000001	1704/11/cnr.17
ISHA SESAY	French presidential frontrunner Marine Le Pen is being slammed for comments about France's role in the Holocaust.	0.32000000000000001	1704/11/cnr.17
ISHA SESAY	I'll talk to an expert on French politics just ahead.	0.14199999999999999	1704/11/cnr.17
ISHA SESAY	Do stay with us.  	0.224	1704/11/cnr.17
ISHA SESAY	  You're watching CNN NEWSROOM live from Los Angeles.	0.21199999999999999	1704/11/cnr.17
ISHA SESAY	I'm Isha Sesay.	0.22600000000000001	1704/11/cnr.17
ISHA SESAY	The headlines this hour: North Korean leader Kim Jong-Un is expected to attend a high profile political gathering.	0.29099999999999998	1704/11/cnr.17
ISHA SESAY	The legislative assembly could give us an idea of Pyongyang's agenda.	0.182	1704/11/cnr.17
ISHA SESAY	The country remains defiant after the U.S. redeployed warships to the Korean Peninsula in response to Pyongyang's nuclear threat.	0.36099999999999999	1704/11/cnr.17
ISHA SESAY	The White House says it won't rule out anything when it comes to Syria.	0.14599999999999999	1704/11/cnr.17
ISHA SESAY	[00:30:00] Earlier Press Secretary Sean Spicer said the Syrian regime's use of barrel bombs would cross a line for the US president.	0.45000000000000001	1704/11/cnr.17
ISHA SESAY	These crude explosives have been used frequently in the six-year civil war.	0.434	1704/11/cnr.17
ISHA SESAY	White House officials later walked back Spicer's comments saying the administration's policy has not changed.	0.246	1704/11/cnr.17
ISHA SESAY	Egyptians are mourning the victims of Sunday's deadly attacks at two Coptic Christian churches.	0.39900000000000002	1704/11/cnr.17
ISHA SESAY	At least 45 people were killed and 125 were wounded.	0.60299999999999998	1704/11/cnr.17
ISHA SESAY	ISIS claimed responsibility and promised more violence.	0.33000000000000002	1704/11/cnr.17
ISHA SESAY	The Egyptian cabinet announced a three-month state of emergency.	0.41899999999999998	1704/11/cnr.17
ISHA SESAY	Swedish officials have released the name of the Uzbek national accused of carrying out Friday's deadly terror attack in Stockholm.	0.38600000000000001	1704/11/cnr.17
ISHA SESAY	39-year- old Rakhmat Akilov is accused of stealing a truck and ploughing it into pedestrians in the Swedish capital.	0.40000000000000002	1704/11/cnr.17
ISHA SESAY	Four people were killed and more than a dozen others wounded.	0.35399999999999998	1704/11/cnr.17
ISHA SESAY	Now, France's far right presidential candidate has sparked an outcry.	0.28199999999999997	1704/11/cnr.17
ISHA SESAY	Marine Le Pen is drawing protests from Jewish groups and the Israeli government after suggesting France was not responsible for the wartime round-up of Jews who were sent to Nazi death camps.	0.47999999999999998	1704/11/cnr.17
ISHA SESAY	The National Front leader says, "I don't think France is responsible for Vel' d'Hiv, a reference to the stadium where thousands of Jews were held before being sent to Auschwitz.	0.40100000000000002	1704/11/cnr.17
ISHA SESAY	Le Pen is the frontrunner in the race for Elysee Palace.	0.251	1704/11/cnr.17
ISHA SESAY	Her election campaign in France officially began on Monday, less than two weeks before the first round of voting on April 23.	0.57999999999999996	1704/11/cnr.17
ISHA SESAY	I'm joined now by Dominic Thomas, Chair of UCLA's Department of French and Francophone Studies.	0.312	1704/11/cnr.17
ISHA SESAY	Dominic, always good to have you with us.	0.14299999999999999	1704/11/cnr.17
ISHA SESAY	So, these comments by Marine Le Pen have really provoked an outcry in France.	0.23599999999999999	1704/11/cnr.17
ISHA SESAY	She has tried to walk them back somewhat saying that she really was saying that the Vichy government wasn't the French government, trying to distance herself on what she said.	0.35399999999999998	1704/11/cnr.17
DOMINIC THOMAS	  I think they're extraordinarily damaging.	0.13400000000000001	1704/11/cnr.17
DOMINIC THOMAS	This is an age- old story.	0.184	1704/11/cnr.17
DOMINIC THOMAS	In 1942, France, remember, the sort of the Free French were in exile in the UK and London with Gen. de Gaulle.	0.55100000000000005	1704/11/cnr.17
DOMINIC THOMAS	And Marshal Petain, in collaboration with the Nazis, was the sort of - named himself sort of the head of the French state.	0.40400000000000003	1704/11/cnr.17
DOMINIC THOMAS	And the French police were ordered by the Nazis to round up Jews.	0.47499999999999998	1704/11/cnr.17
DOMINIC THOMAS	Lists that had been created by the Nazis, over 13,000 went to Vel' d'Hiv and were deported, obviously, to the camps in Auschwitz and never returned.	0.68899999999999995	1704/11/cnr.17
DOMINIC THOMAS	For a very long time, the far right in France has embraced the figure of Petain as a sort of greatness.	0.32200000000000001	1704/11/cnr.17
DOMINIC THOMAS	And Marine Le Pen has got herself caught up here.	0.186	1704/11/cnr.17
DOMINIC THOMAS	She is, on the one hand, trying to sort of talk about making France great again and, therefore, finds herself sort of having to talk about great historical figures and the sort of the great past and all these kinds of questions.	0.30299999999999999	1704/11/cnr.17
DOMINIC THOMAS	What she's tried to do for the last few years is to clean up the party image and to modernize the image.	0.215	1704/11/cnr.17
DOMINIC THOMAS	She's gone so far as to kick her father out of the party, who himself has a very long history of being both criminalized and sentenced for making outrageous comments.	0.28799999999999998	1704/11/cnr.17
DOMINIC THOMAS	The most notable comment is to basically say that the gas chambers were a detail in the Second World War.	0.39900000000000002	1704/11/cnr.17
DOMINIC THOMAS	So, she's tried to appeal to a broader mainstream and her base - or certain elements of the party still hold on to these strong anti-Semitic kind of traits.	0.14699999999999999	1704/11/cnr.17
DOMINIC THOMAS	But she can't get elected by appealing to them. 	0.153	1704/11/cnr.17
And what she's been trying to do for the past several months is to appeal to a broader base of people	  So, let me be clear.	0.070999999999999994	1704/11/cnr.17
And what she's been trying to do for the past several months is to appeal to a broader base of people	If the math makes it clear, she can't be voted by her base alone, should we say that these comments were her misspeaking or was there a political strategy at play here, kind of dog-whistle, if you will	0.129	1704/11/cnr.17
DOMINIC THOMAS	  I can't see what the political strategy would be because her base puts her somewhere in the mid-20s.	0.122	1704/11/cnr.17
DOMINIC THOMAS	If she makes it through to the second round, which she has a very good chance of getting there because of this base support, she needs to get over 50 percent to be elected.	0.34799999999999998	1704/11/cnr.17
DOMINIC THOMAS	And people are being increasingly comforted to sort of supporting her.	0.24199999999999999	1704/11/cnr.17
DOMINIC THOMAS	She participated in the first-round debate.	0.32100000000000001	1704/11/cnr.17
DOMINIC THOMAS	She's become increasingly legitimate when she speaks about immigration, anti-EU and so on.	0.16	1704/11/cnr.17
DOMINIC THOMAS	But to go back to these kinds of comments, anti-Semitic comments, questionings or questions around the sort of the Second World War is highly problematic and actually really goes against everything she's been trying to do over the past few years.	0.39300000000000002	1704/11/cnr.17
DOMINIC THOMAS	In the past few years, when someone in her party made an outrageous racist comment or an anti-Semitic comment, she could take the high ground, discipline them, remove them from the party and distance herself by saying this is no longer what we stand for.	0.16800000000000001	1704/11/cnr.17
DOMINIC THOMAS	But she's fallen into the same trap.	0.19400000000000001	1704/11/cnr.17
DOMINIC THOMAS	And I think the trap is being created by her to the extent that people are interested in how she reconciles this claim for nationalism, what people have called it kind of ethno-nationalism, this white Christian France without at the same time distancing herself from some of the darker chapters in French history.	0.32300000000000001	1704/11/cnr.17
DOMINIC THOMAS	[00:35:10] 	0.42299999999999999	1704/11/cnr.17
ISHA SESAY	  As we know, Marine Le Pen has been leading in the polls.	0.34100000000000003	1704/11/cnr.17
ISHA SESAY	Let me ask you how the polls look now with elections two weeks away.	0.183	1704/11/cnr.17
ISHA SESAY	We are seeing some movement. 	0.34100000000000003	1704/11/cnr.17
DOMINIC THOMAS	  Yes.	0.40600000000000003	1704/11/cnr.17
DOMINIC THOMAS	We are seeing some movement.	0.34100000000000003	1704/11/cnr.17
DOMINIC THOMAS	The interesting thing - and we've talked about this before - is that the French have never held debates in the first round.	0.34499999999999997	1704/11/cnr.17
DOMINIC THOMAS	They've always waited till the second round.	0.32900000000000001	1704/11/cnr.17
DOMINIC THOMAS	And the debate that took place last week, that brought all 11 presidential candidates together, really allowed some of them to sort of set themselves up.	0.437	1704/11/cnr.17
DOMINIC THOMAS	And they also took a lot of criticism from the minor characters.	0.32500000000000001	1704/11/cnr.17
DOMINIC THOMAS	And so, on the left, the socialist candidate Hamon underperformed in these debates, but is also in many ways being held responsible for the disastrous legacy, one should say, of the Hollande presidency, has really gone down in the polls to single digits.	0.55400000000000005	1704/11/cnr.17
DOMINIC THOMAS	And the far left candidate who did not participate in the primary, Jean-Luc Melenchon, who used to be a socialist, but is really far closer to the Communist Party, has risen up in the polls.	0.41899999999999998	1704/11/cnr.17
DOMINIC THOMAS	Fillon is still sort of holding around the 15 percent or 18 percent, but the corruption scandal is not helping him.	0.628	1704/11/cnr.17
DOMINIC THOMAS	The far right is relatively stable.	0.20999999999999999	1704/11/cnr.17
DOMINIC THOMAS	And Macron has remained relatively stable. 	0.28000000000000003	1704/11/cnr.17
ISHA SESAY	  But not growing. 	0.22500000000000001	1704/11/cnr.17
DOMINIC THOMAS	  Not growing.	0.253	1704/11/cnr.17
DOMINIC THOMAS	And this is the big issue, is that we've gone from what looked like a two race between Macron and Le Pen a few weeks ago to now there being four candidates that are dividing up these votes and are at somewhere between the 17 percent, 18 percent and 25 percent, which means - and also people are just disillusioned with this whole election.	0.82599999999999996	1704/11/cnr.17
DOMINIC THOMAS	The corruption scandal - 	0.16300000000000001	1704/11/cnr.17
ISHA SESAY	  Penelopegate, all of the - 	0.16800000000000001	1704/11/cnr.17
DOMINIC THOMAS	  Penelopegate.	0.23000000000000001	1704/11/cnr.17
DOMINIC THOMAS	All these kinds of things.	0.14499999999999999	1704/11/cnr.17
DOMINIC THOMAS	There are a lot of undecided voters and also a very large portion of the - a significant number of voters have said they're not even going to bother voting or destroy their ballot and so on.	0.26800000000000002	1704/11/cnr.17
DOMINIC THOMAS	So, the outcome really at this stage remains unpredictable.	0.19500000000000001	1704/11/cnr.17
DOMINIC THOMAS	And I don't think anybody can honestly say who will be there in the second round.	0.084000000000000005	1704/11/cnr.17
DOMINIC THOMAS	The fact remains they still all believe they can beat Le Pen, so they all want to get to that second round.	0.16300000000000001	1704/11/cnr.17
DOMINIC THOMAS	And she hasn't helped herself with this latest round of problematic comments.	0.20100000000000001	1704/11/cnr.17
DOMINIC THOMAS	That's for sure. 	0.185	1704/11/cnr.17
ISHA SESAY	  Dominic, you've been helping us make sense of it.	0.221	1704/11/cnr.17
ISHA SESAY	You will be in France - 	0.122	1704/11/cnr.17
DOMINIC THOMAS	  Absolutely. 	0.182	1704/11/cnr.17
ISHA SESAY	  -- as they go to the polls.	0.218	1704/11/cnr.17
ISHA SESAY	We appreciate it always. 	0.17499999999999999	1704/11/cnr.17
DOMINIC THOMAS	  I look forward to it.	0.17299999999999999	1704/11/cnr.17
DOMINIC THOMAS	Thank you, Isha. 	0.14899999999999999	1704/11/cnr.17
ISHA SESAY	  Thank you. 	0.14799999999999999	1704/11/cnr.17
DOMINIC THOMAS	  Thanks. 	0.19600000000000001	1704/11/cnr.17
ISHA SESAY	  Quick break here.	0.27500000000000002	1704/11/cnr.17
ISHA SESAY	Coming up, the not-so-friendly skies.	0.23699999999999999	1704/11/cnr.17
ISHA SESAY	United Airlines is responding after a paying customer was dragged off.	0.41699999999999998	1704/11/cnr.17
ISHA SESAY	That's right.	0.20599999999999999	1704/11/cnr.17
ISHA SESAY	Dragged off a flight.  	0.26900000000000002	1704/11/cnr.17
ISHA SESAY	  Hello everyone.	0.214	1704/11/cnr.17
ISHA SESAY	The US Department of Transportation is reviewing an extremely disturbing incident on United Airlines flight.	0.36399999999999999	1704/11/cnr.17
ISHA SESAY	A passenger who refused to give up his seat on an overbooked flight was forcibly dragged off the plane and it was all caught on video.	0.377	1704/11/cnr.17
ISHA SESAY	Watch.	0.28799999999999998	1704/11/cnr.17
ISHA SESAY	[00:40:05] 	0.38200000000000001	1704/11/cnr.17
ISHA SESAY	  You can see quite clearly security officers janging (ph) the man from his seat on a flight bound to Kentucky, Sunday.	0.19900000000000001	1704/11/cnr.17
ISHA SESAY	Other passenger videos shows him with a bloodied mouth.	0.314	1704/11/cnr.17
ISHA SESAY	The airline says it needed the space for four crew members.	0.434	1704/11/cnr.17
ISHA SESAY	Officials have placed one of the security officers on leave pending a review.	0.38900000000000001	1704/11/cnr.17
ISHA SESAY	Well, United CEO released this statement.	0.224	1704/11/cnr.17
ISHA SESAY	"This is an upsetting event to all of us here at United.	0.14999999999999999	1704/11/cnr.17
ISHA SESAY	I apologize for having to re-accommodate these customers.	0.20300000000000001	1704/11/cnr.17
ISHA SESAY	Our team is moving with a sense of urgency to work with the authorities and conduct our own detailed review of what happened."	0.24299999999999999	1704/11/cnr.17
ISHA SESAY	I'm pleased to say I'm joined now by defense attorney Sara Azari.	0.26500000000000001	1704/11/cnr.17
ISHA SESAY	Thank you so much for joining us.	0.20799999999999999	1704/11/cnr.17
ISHA SESAY	Let me just start with just that statement.	0.158	1704/11/cnr.17
ISHA SESAY	What is that	0.121	1704/11/cnr.17
SARA AZARI	  That's like the least of their worries, right	0.14099999999999999	1704/11/cnr.17
ISHA SESAY	  So, that is clearly illegal because he was already in a seat - 	0.186	1704/11/cnr.17
SARA AZARI	  They had put him on the plane.	0.26800000000000002	1704/11/cnr.17
SARA AZARI	And the only time they can eject you in that situation from the flight is if you pose a terrorist threat, if you are drunk and obnoxious or you're a safety threat to yourself or others, or there is some medical emergency.	0.11700000000000001	1704/11/cnr.17
SARA AZARI	None of those exceptions applied here.	0.27900000000000003	1704/11/cnr.17
SARA AZARI	So, this is a classic case of an airline overselling.	0.251	1704/11/cnr.17
SARA AZARI	And I have a serious problem with that as a traveler myself.	0.20200000000000001	1704/11/cnr.17
SARA AZARI	They oversell.	0.25600000000000001	1704/11/cnr.17
SARA AZARI	They overbook.	0.25600000000000001	1704/11/cnr.17
SARA AZARI	And in this case, they made the mistake of not addressing that issue before everyone boarded. 	0.25700000000000001	1704/11/cnr.17
ISHA SESAY	  What about those people who are saying .	0.16200000000000001	1704/11/cnr.17
ISHA SESAY	I know that some people may be saying, well, they asked him to get up, they - it's within - the airline - is it in the airline small print	0.34899999999999998	1704/11/cnr.17
SARA AZARI	  At this point, they really need to hope that people would do this voluntarily.	0.12	1704/11/cnr.17
SARA AZARI	And nobody - they offered $400, $800 and then $1,000.	0.71799999999999997	1704/11/cnr.17
SARA AZARI	Nobody would volunteer to get off.	0.152	1704/11/cnr.17
SARA AZARI	This is a Sunday night.	0.155	1704/11/cnr.17
SARA AZARI	People want to get home, people want to get to work on Monday morning.	0.16	1704/11/cnr.17
SARA AZARI	Nobody was going to do this voluntarily.	0.17100000000000001	1704/11/cnr.17
SARA AZARI	So, then they resorted to - we're going to involuntarily ask for people to leave to accommodate these crew members. 	0.191	1704/11/cnr.17
ISHA SESAY	  Any clue on how they chose the four people	0.125	1704/11/cnr.17
SARA AZARI	  It's interesting.	0.24399999999999999	1704/11/cnr.17
SARA AZARI	I was looking into that.	0.191	1704/11/cnr.17
SARA AZARI	And it doesn't seem to be - there is a system in place.	0.183	1704/11/cnr.17
SARA AZARI	And it appears to be a combo of random selection by the computer as well as employees.	0.188	1704/11/cnr.17
SARA AZARI	Like, for instance, if you're a family, they try not to break up the family.	0.17000000000000001	1704/11/cnr.17
SARA AZARI	They try to keep you together, if you're traveling together.	0.11	1704/11/cnr.17
SARA AZARI	So, obviously, this man was by himself.	0.155	1704/11/cnr.17
SARA AZARI	So, he was sort of the - probably one of the first choices of people to boot out.	0.29699999999999999	1704/11/cnr.17
SARA AZARI	And also, it's about your destination, how long you have to wait for the next flight to that destination. 	0.17799999999999999	1704/11/cnr.17
ISHA SESAY	  Although we are hearing, he was actually with his wife on that flight. 	0.312	1704/11/cnr.17
SARA AZARI	  Oh, well, then - 	0.14499999999999999	1704/11/cnr.17
ISHA SESAY	  So, the whole - again, it is all so murky.	0.10199999999999999	1704/11/cnr.17
ISHA SESAY	So, tell me, in terms of legal options for him, the expectation is there will be lawsuit.	0.155	1704/11/cnr.17
ISHA SESAY	What would that look like	0.057000000000000002	1704/11/cnr.17
SARA AZARI	  Well, first of all, the Department of Transportation allows him to recover up to four times the amount of his travel costs, which - to me, this is way beyond that.	0.36099999999999999	1704/11/cnr.17
SARA AZARI	Civil lawsuit, because there was excessive force used and it's humiliating and he was bleeding.	0.35499999999999998	1704/11/cnr.17
SARA AZARI	It was awful what we saw on video.	0.191	1704/11/cnr.17
SARA AZARI	And then also, I think I would try to push for some criminal prosecution too.	0.14000000000000001	1704/11/cnr.17
SARA AZARI	There were no exceptions against the airline and the security officers because it's essentially assault battery when there is no justification for them to use this kind of force on this man.	0.36599999999999999	1704/11/cnr.17
SARA AZARI	It was really sort of out of line.	0.28499999999999998	1704/11/cnr.17
SARA AZARI	People forget that today we have smartphones and we get to document everything. 	0.27700000000000002	1704/11/cnr.17
ISHA SESAY	  It's a distressing video.	0.246	1704/11/cnr.17
ISHA SESAY	Every time I see it, every time I hear it, I find it very difficult to watch.	0.11700000000000001	1704/11/cnr.17
ISHA SESAY	Sara, we appreciate you just explaining what lies ahead, what potentially lies ahead and just how out of the norm this was. 	0.19800000000000001	1704/11/cnr.17
SARA AZARI	  It's very unusual, yes.   	0.36899999999999999	1704/11/cnr.17
ISHA SESAY	  Thank you. 	0.14799999999999999	1704/11/cnr.17
SARA AZARI	  Thank you. 	0.14799999999999999	1704/11/cnr.17
ISHA SESAY	  All right.	0.192	1704/11/cnr.17
ISHA SESAY	And thank you for watching CNN NEWSROOM live from Los Angeles, in fact.	0.24199999999999999	1704/11/cnr.17
ISHA SESAY	I'm Isha Sesay.	0.22600000000000001	1704/11/cnr.17
ISHA SESAY	"World Sport" is up next.	0.29199999999999998	1704/11/cnr.17
ISHA SESAY	And I'll be back with another hour of NEWSROOM all around the world.	0.161	1704/11/cnr.17
ISHA SESAY	You're watching CNN.	0.23499999999999999	1704/11/cnr.17
ISHA SESAY	[00:45:12]    	0.41499999999999998	1704/11/cnr.17
\.


--
-- TOC entry 2101 (class 0 OID 0)
-- Dependencies: 6
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2017-04-12 01:24:10

--
-- PostgreSQL database dump complete
--

